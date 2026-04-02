
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os 
from pathlib import Path
import inoutput as io
import json


os.chdir(Path(__file__).parent)

cred = credentials.Certificate("grapefruit256-27d68-ac12fab9e41d.json") # std
#cred_L = credentials.Certificate("grapefruit256-27d68-0c7120b87ef0.json") L
#cred_Lu = credentials.Certificate("grapefruit256-27d68-6df1a5302848.json") Lu - falls ich sie brauchen werde !


dbEnd = True
try:
    firebase_admin.initialize_app(cred)
except ValueError as e:
    print(f"Initialisation Check of service account: {e}")
    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
    #print("try1 - raise ValueError",dbEnd)


try:
    token = cred.get_access_token().access_token  # Abrufen des Access Tokens
    if token:  # Wenn kein Token gefunden wird, ist das Zertifikat ungültig
        raise ValueError('Service account certificate valid - no new pentis version required')
    
    #print("try2 - token - raise ValueError", dbEnd)

except ValueError as e:
    print(f"Checking service account: {e}")
    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
except Exception as e:
    print(f"Service account certificate not valid anymore - new pentis version download required: {e}")
    dbEnd = False
    #print("newVersion:", dbEnd)

    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
#else:
#    print("Der Schlüssel des Firebase-Dienstkontos ist ungültig.")


#app = firebase_admin.initialize_app(cred)
# Zugriff auf firestore
if dbEnd == False:
        io.keyBox()

# *********************************JSONs*****************************



file_path_iText = os.path.join(os.path.expanduser('~'), 'Pentis', 'iText.json')

def writeJS(dict): #ex fileWriteJS()
    # Data in eine JSON-Datei schreiben
    with open(file_path_iText, "w") as datei:
        #json.dump(dict, datei)
        json.dump(dict, datei, indent=2, ensure_ascii=False, separators=(',', ': ')) #, newline='\n'

#writeJS(iText)

def readJS(filePath):
    with open(filePath, "r") as datei:        # Vorsicht file_path = path UND die (json)-Datei
    #with open(filePath, "r", encoding="utf-8") as datei:        # Vorsicht file_path = path UND die (json)-Datei
        dataJS = json.load(datei)    
    return dataJS

#iText2 = readJS(file_path_iText)

#print(iText)
#print(iText2)

# ******************************FIREBASE******************************

db = firestore.client()

name = "Norbert Noname"
score = 2057


def addHighscore(dataMode, name, score):
    #dataMode = dataMode - 11
    #modeList = ["pentis0800_novice","pentis0722_std", "pentis0722_L", "pentis0722_Lu"] # 0722 weil die DB für 0722 erstellt wurden
    modeDict = {9: "pentis0800_novice", 11: "pentis0722_std", 12: "pentis0722_L", 13: "pentis0722_Lu"} # 0722 weil die DB für 0722 erstellt wurden
    scores_ref = db.collection(modeDict[dataMode])
    query = scores_ref.where("name", "==", name)
    results = query.get()

    if len(results) > 0:
        for doc in results:
            if doc.to_dict()["score"] >= score:
                print(f"{name} is already in the collection with a higher score.")
            else:
                doc.reference.update({"score": score})
                print(f"{name} has been updated with the new score.")
    else:
        scores_ref.add({
            "name": name,
            "score": score
        })
        print(f"{name} has been added to the collection.")
    #return dbEnd



def getHighscores(dataMode):
    #dataMode = dataMode - 11
    #modeList = ["pentis0800_novice","pentis0722_std", "pentis0722_L", "pentis0722_Lu"]
    modeDict = {9: "pentis0800_novice", 11: "pentis0722_std", 12: "pentis0722_L", 13: "pentis0722_Lu"} # 0722 weil die DB für 0722 erstellt wurden   
    scores = []
    scores_ref = db.collection(modeDict[dataMode])
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(10)
    # query2 für ranks 11-20 !
    #query2 = scores_ref.where("rank", ">=", 10).where("rank", "<=", 20).order_by("rank").limit(11) # limit(11) da inklusive 10 und 20 also 11 werte
    for doc in query.stream():
    #for doc in query2.stream():
        scores.append(doc.to_dict())
    print("inner GetHighscores return scores",scores)
    return scores

def getHighscores20(dataMode):
    modeDict = {9: "pentis0800_novice", 11: "pentis0722_std", 12: "pentis0722_L", 13: "pentis0722_Lu"}
    scores = []
    scores_ref = db.collection(modeDict[dataMode])
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(20)
    #print(query)
    for doc in query.stream():
        scores.append(doc.to_dict())
    return scores

def getHighscores20_bkp(): #pre datamode adaptation
    scores = []
    scores_ref = db.collection("pentis0722_std")
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(20)
    #print(query)
    for doc in query.stream():
        scores.append(doc.to_dict())
    return scores


def printHighscoresManually():
    i = 0
    scores = []
    scores_ref = db.collection("pentis0722_std")     # scores_ref = <google.cloud.firestore_v1.collection.CollectionReference object at 0x00000216853A1340>
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(10)
    for doc in query.stream():                  # doc = <google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x00000160173A3E50>
        scores.append(doc.to_dict())
    print("Name" + "\t\t\tScore")
    for i in range(len(scores)):
        print(scores[i]["name"] + "\t\t\t", scores[i]["score"])    
        


# nur um alle highscores bis 20 in shell zu checken
allScores = getHighscores20(11)
print(allScores)
#print("fbRW: Number 1: ", allScores[0])
#print("fbRW: Last score: ", allScores[-1]["score"])

""" rankdata = {"name": "Pete", "score": 111458 }
def writeFunc(data):
    db.collection("pentisLab").document("highscores").set(data)
def readFunc():
    result2 = db.collection("pentisLab").document("highscores").get()
    print(result2.to_dict()) """
#writeFunc(rankdata)
#readFunc()


