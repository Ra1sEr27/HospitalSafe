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

import getpass
client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
db = client["Hospital"]   
mycol = db["CTonly"]
'''
db.createView(
   "managementFeedback",
   "survey",
   [ { $project: { "management": "$feedback.management", department: 1 } } ]
)
'''
item_details = mycol.find()
templist = []
thislist = []
no =0
for item in item_details:
    # This does not give a very readable output
    templist.append(item)
    thislist.append(templist[no]['CT'])
    no = no +1
#print(thislist)
#print(len(thislist))
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
def findpatient_info_byid(Patient_id,section):
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
            print("Room: ",declist[i]["Room"])
            break
        elif (i==len(declist)-1): #the last patient name in list is not matched with the inputted name
            print("No patient record") 

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
    #print(declist)
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
            print("Room: ",declist[i]["Room"])
            break
    
        elif (i==len(declist)-1): #the last patient name in list is not matched with the inputted name
            print("No patient record") 
		
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
    count = 0
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
            count = count +1
        elif age > int (real_age):
            pass
    print('There are' +count+' people')

def find_room(roomNo,section):
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
        if (declist[i]["Room"] == str(roomNo)):
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
            print("Room: ",declist[i]["Room"])
            break

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
        if (declist[i]["nationality"] <= height):
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
        if (declist[i]["nationality"] <= weight):
            templist.append(declist[i])
    No = len(templist)
    print("There are ",No,"people.")
    print("test------------------------------",type(templist))
    for i in range(len(templist)):
        print(templist[i]["name"] + "------------>" + templist[i]["weight"] + 'kg')
    return templist

    
def getview(section):
    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    db = client["Hospital"]   
    mycol = db["CTonly"+str(section)]

    item_details = mycol.find()
    templist = []
    global thislist 
    thislist= []
    no =0
    for item in item_details:
        # This does not give a very readable output
        templist.append(item)
        thislist.append(templist[no]['CT'])
        no = no +1

    while(True):
        test = input("Which type of patient data you want to know? (information, nationality, bloodtype, age, room): ")
        test.lower()
        #print(section)
        #print(type(section))
        if test not in ("information", "nationality", "bloodtype", "age", "room", "back","exit"):
            print("Invalid type of data")
        elif test == "exit":
            exit()
        elif test == "back":
            break
        if (test == "information"):
            second = input("Search by name or id: ")
            if (second == "id"):
                pad = input("Patient's ID: ")
                findpatient_info_byid(pad,section)
            elif (second == "name"):
                pan = input("Patient's name: ")
                findpatient_info_byname(pan,section)
            else:
                print("invalid input")
        elif (test == "nationality"):
            patientnationality = input("Insert nationality: ")
            findall_nationality(patientnationality,section)
        elif (test == "bloodtype"):
            patientblood = input("Insert bloodtype: ")
            findall_bloodtype(patientblood,section)
        elif (test == "age"):
            patientage = input("Insert age: ")
            findall_ageofpatients_below(patientage,section)
        elif (test == "height"):
            patientage = input("Insert height: ")
            findall_height(patientage,section)
        elif (test == "weight"):
            patientage = input("Insert wieght: ")
            findall_weight(patientage,section)
        elif (test == "room"):
            patientroom = input("Insert patient's room: ")
            find_room(patientroom,section)

        else:
            print("The command does not exist, please try again")