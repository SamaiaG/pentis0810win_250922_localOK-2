import os
from pathlib import Path
os.chdir(Path(__file__).parent)

username = "Samuel"
data=open("username.txt","w")
data.write(username)


""" 
for count in range(10):
    data.write(str(count))
    data.write("\n")
    print(data) """