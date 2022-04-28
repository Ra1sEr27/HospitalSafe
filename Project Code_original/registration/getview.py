#this imports the cryptography package
from cryptography.fernet import Fernet
import json
#binasc
import sys
import symcrytjson
from datetime import date
#from cloudant import couchdb_admin_party
#from cloudant.result import Result
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
db = client["Hospital"]   
mycol = db["CTonly"]

print(db.mycol.find())
#for dbname in db:
#    print(dbname)
#db = couch["hospital_section1"]
#thislist = []
#for item in db.view('onlyCT/CTview'):
    #thislist.append(item.key)
    #print(item.key)
    #print(type(item.key))
#print(thislist)
#print(len(thislist))
#print("this1:",thislist[0])
#print("this2:",thislist[1])
#print("---------------------------------")
#print(thislist[0])
'''
with open('section1_staff.key', 'rb') as file:
   	key = file.read()
testbyte = str.encode(thislist[0])
fernet = Fernet(key)
decdoc = fernet.decrypt(testbyte)
#print(decdoc)
#print(type(decdoc))

data = decdoc.decode('UTF-8')
#print(data)
data = json.loads(data)
#print(type(data))
#print(data["name"])
#print(type(data["name"]))   
'''
def findpatient_info(Patient_Name):
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        #print(decdoc)
        #print(type(decdoc))
        #print(decdoc.decode('UTF-8'))
        #print("name1:", declist[0]["name"])
        #print(len(declist))
        #print("---------------------------------")
        #print(declist)
        #print("---------------------------------")
    print("test:",len(declist))
    for i in range(len(declist)):
        if (declist[i]["name"] == str(Patient_Name)):
            print(declist[i]["name"])
            print(declist[i]["dob"])
            print(declist[i]["RelativePhonenum"])
            print(declist[i]["nationality"])
            print(declist[i]["status"])
            print(declist[i]["height"])
            print(declist[i]["weight"])
            print(declist[i]["bloodtype"])
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
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        print("test--------------------------:",len(declist))
        #print(decdoc)
        #print(type(decdoc))
        #print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["nationality"] == Nationality):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people.")
    print("test------------------------------",type(templist))
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["nationality"])
    return templist

def findall_bloodtype(blood):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        print("test--------------------------:",len(declist))
        #print(decdoc)
        #print(type(decdoc))
        #print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["bloodtype"] == blood):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people.")
    print("test------------------------------",type(templist))
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["blood"])
    return templist

def findall_ageofpatients_below(real_age):
    current_year = date.today().year
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        print("test--------------------------:",len(declist))
    for i in range(len(declist)):
        dob = declist[i]["dob"]
        year = int(dob[6:])
        age = current_year - year
        #print("current:",current_year)
        #print("year",year)
        #print("age:",age)
        if age <= int(real_age):
            print(declist[i]["name"])
            print(declist[i]["dob"])
            print("Age =", age) 
        else:
            print("no one")

def findall_height(height):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        print("test--------------------------:",len(declist))
        #print(decdoc)
        #print(type(decdoc))
        #print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["nationality"] == height):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people.")
    print("test------------------------------",type(templist))
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["height"] + 'cm')
    return templist

def findall_weight(weight):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section1_staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
        print("test--------------------------:",len(declist))
        #print(decdoc)
        #print(type(decdoc))
        #print(decdoc.decode('UTF-8'))
    for i in range(len(declist)):
        if (declist[i]["nationality"] == weight):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people.")
    print("test------------------------------",type(templist))
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["weight"] + 'kg')
    return templist

test = input("what do you want to know?")
if (test == "patient_info"):
    patientname = input("Insert the name:")
    findpatient_info(patientname)
elif (test == "patient_nationality"):
	patientnationality = input("Insert nationality:")
	findall_nationality(patientnationality)
elif (test == "patient_bloodtype"):
	patientblood = input("Insert bloodtype:")
	findall_bloodtype(patientblood)
elif (test == "patient_age"):
	patientage = input("Insert age:")
	findall_ageofpatients_below(patientage)
else:
    print("The command does not exist, please try again")