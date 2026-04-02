import firebase_admin
from firebase_admin import credentials
#from firebase_admin import db
from firebase_admin import firestore

from prettytable import PrettyTable
import os 
from pathlib import Path

os.chdir(Path(__file__).parent)
# initialize the Firebase app
cred = credentials.Certificate("..\\grapefruit256-27d68-firebase-adminsdk-remzi-0024cf9c1d.json")
app = firebase_admin.initialize_app(cred)
#firebase_admin.initialize_app(cred, {
#    'databaseURL': 'https://your-database-name.firebaseio.com'
#})
db = firestore.client()
# get a reference to the database
ref = db.collection("pentisLab")

# retrieve the data as a dictionary
data = ref.get()

# get the column names
columns = list(data[0].keys())

# create a PrettyTable object with the column names
table = PrettyTable(columns)

# add the rows to the table
for row in data:
    table.add_row(list(row.values()))

# print the table
print(table)

