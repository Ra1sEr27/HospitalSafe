import keygenerator
import couchdb
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import os
import symcrytjson
import registrar

sec = input("insert data to section? : ")

doc = {"id":"01000",
        "name":"Roman",
        "National ID":"110150333212",
        "Addres of residence":"Bangkok",
        "Phonenum":"0883334444",
        "Email":"Roman@gmail.com",
        "Name of family member":"Hubby",
        "Contact of family member":"0338889999",
        "dob":"01/04/1999",
        "nationality":"Thailand",
        "height": "180",
        "weight":"70",
        "bloodtype":"A",
        "Insurance Provider":"AIA",
        "Insurance ID":"A12500",
        "Responsible Physician":"Rygan",
        "Health-related behavior":"-",
        "Past medical records":"-",
        "Family history":"-",
        "Allergies":"Carrot"}

staff_doc = {
   "id": "m150",
   "name": "Daniel Charn",
   "password": "pass",
   "role": "registrar",
   "accessdb": "section{}_staff".format(sec)
}

try:
    # connect to the DB
    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    db = couch['hospital_section{}'.format(sec)] # main
    staff_db = couch['section{}_staff'.format(sec)] # main
        
except(couchdb.http.Unauthorized):
    print("Invalid username or password")

with open('section{}_staff.key'.format(sec),'rb') as file:
    key = file.read()

#covert JSON to string
doc_string = json.dumps(doc)

doc_encrypted = symcrytjson.encryptjson(key,doc_string) 

doc_string1 = json.dumps(staff_doc)

doc_encrypted1 = symcrytjson.encryptjson(key,doc_string1) 

db.save(doc_encrypted)
staff_db.save(doc_encrypted1)

