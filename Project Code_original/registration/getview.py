#this imports the cryptography package
from cryptography.fernet import Fernet
import json
#binasc
import sys
from datetime import date
#from cloudant import couchdb_admin_party
#from cloudant.result import Result
from pymongo import MongoClient
import pymongo
import timeit
import index
import getpass
client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
db = client["Hospital"]   
mycol = db["CTonly"]

item_details = mycol.find()
templist = []
thislist = []
no =0
for item in item_details:
    # This does not give a very readable output
    templist.append(item)
    thislist.append(templist[no]['CT'])
    no = no +1
print(thislist)
print(len(thislist))
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
with open('section1-staff.key', 'rb') as file:
    key = file.read()
testbyte = str.encode(thislist[0])
fernet = Fernet(key)
decdoc = fernet.decrypt(testbyte)
print(decdoc)
print(type(decdoc))

data = decdoc.decode('UTF-8')
#print(data)
data = json.loads(data)
#print(type(data))
#print(data["name"])
#print(type(data["name"]))   
'''
def findpatient_info_byid(Patient_id, section):
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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
        if (declist[i]["id"] == str(Patient_id)):
            print("ID: ", declist[i]["id"])
            print("Name: ",declist[i]["name"])
            print("Family member: ",declist[i]["Name of family member"])
            print("Family member contact: ",declist[i]["Contact of family member"])
            print("Date of birth: ",declist[i]["dob"])
            print("Nationality: ",declist[i]["nationality"])
            print("Height: ",declist[i]["height"]," cm")
            print("Weight: ",declist[i]["weight"]," kg")
            print("Bloodtype: ",declist[i]["bloodtype"])
            print("Insurance Provider: ",declist[i]["Insurance Provider"])
            print("Insurance ID: ",declist[i]["Insurance ID"])
            print("Responsible Physician: ",declist[i]["Responsible Physician"])
            print("Health-related behavior: ",declist[i]["Health-related behavior"])
            print("Past medical records: ",declist[i]["Past medical records"])
            print("Allergies: ",declist[i]["Allergies"])
            break
        else:
            print("no patient record") 

def findpatient_info_byname(Patient_Name,section):
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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
            print("ID: ", declist[i]["id"])
            print("Name: ",declist[i]["name"])
            print("Family member: ",declist[i]["Name of family member"])
            print("Family member contact: ",declist[i]["Contact of family member"])
            print("Date of birth: ",declist[i]["dob"])
            print("Nationality: ",declist[i]["nationality"])
            print("Height: ",declist[i]["height"]," cm")
            print("Weight: ",declist[i]["weight"]," kg")
            print("Bloodtype: ",declist[i]["bloodtype"])
            print("Insurance Provider: ",declist[i]["Insurance Provider"])
            print("Insurance ID: ",declist[i]["Insurance ID"])
            print("Responsible Physician: ",declist[i]["Responsible Physician"])
            print("Health-related behavior: ",declist[i]["Health-related behavior"])
            print("Past medical records: ",declist[i]["Past medical records"])
            print("Allergies: ",declist[i]["Allergies"])
            break
        else:
            print("no patient record") 
		
def findall_nationality(Nationality,section):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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
    for i in range(len(declist)):
        if (declist[i]["nationality"] == Nationality):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people. ")
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["nationality"])
    return templist

def findall_bloodtype(blood,section):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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
        print(templist[i]["name"] + "------------>" + templist[i]["bloodtype"])
    return templist

def findall_ageofpatients_below(real_age,section):
    current_year = date.today().year
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
            key = file.read()
        testbyte = str.encode(thislist[i])
        fernet = Fernet(key)
        decdoc = fernet.decrypt(testbyte)
        data = decdoc.decode('UTF-8')
        data = json.loads(data)
        declist.append(data)
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
        elif age > int (real_age):
            pass

def findall_height(height,section):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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

def findall_weight(weight,section):
    templist = []
    declist = []
    for i in range (len(thislist)):
        with open('section'+str(section)+'-staff.key', 'rb') as file:
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

while(True):
    index()
    test = input("what do you want to know?")
    if (test == "patient_info"):
        second = input("Search by name or ID:")
        if (second == "ID"):
            input = input("Patien's iD:")
            findpatient_info_byid(input)
        elif (second == "name"):
            input = input("Patient's name:")
            findpatient_info_byname(input)
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