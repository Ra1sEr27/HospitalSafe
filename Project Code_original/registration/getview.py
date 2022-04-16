#this imports the cryptography package
from cryptography.fernet import Fernet
import getpass
import couchdb
import hashlib, hmac
#binasc
import sys
import symcrytjson
#from cloudant import couchdb_admin_party
#from cloudant.result import Result

username = 'nontawat'
password = 'non123'
couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))

for dbname in couch:
    print(dbname)
db = couch["hospital_section1"]
thislist = []
for item in db.view('onlyCT/CTview'):
    thislist.append(item.key)
    print(item.key)
    print(type(item.key))

print("---------------------------------")
print(thislist[0])

with open('section1_staff.key', 'rb') as file:
   	key = file.read()
       
def findpatient_info(Patient_Name):
    declist = []
    
    for i in range (len(thislist)):
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        declist.append(decdoc)
        print(decdoc)
        print(type(decdoc))
        print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["Name"] == Patient_Name):
            print(declist[i])
            break
        else:
            print("no patient record") 	
		
def findall_nationality(Nationality):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        declist.append(decdoc)
        print(decdoc)
        print(type(decdoc))
        print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["Nationality"] == Nationality):
            templist.append(declist[i])
    print(templist)
    return templist
