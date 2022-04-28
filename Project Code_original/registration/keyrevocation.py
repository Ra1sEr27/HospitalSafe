import keygenerator
import couchdb
from cryptography.fernet import Fernet
from pymongo import MongoClient
import pymongo
import couchdb
import json
import os
import symcrytjson
import registrar

def keyrevocation(target_section):
    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
    mydb = client['Hospital']
    with open('section{}-staff.key'.format(target_section),'rb') as file2:
        old_key = file2.read() #keep the old key for generating MD
    while(True):
        #target_section = input("Enter the compromised section (0-3) : ")
        if target_section == "0":   #target section = admin section
            keygenerator.re_adminkeygenerator()
            db = mydb["admin"]
            break
        elif target_section in ("1","2","3"):
            keygenerator.re_staffkeygenerator(target_section)
            staffcol = mydb["section{}-staff".format(target_section)]
            patientcol = mydb["section{}-patient".format(target_section)]
            break
        else:
            print("Invalid section, please try again")
            break
    #for docid in staffcol.find(): #delete all documents in compromised staff section
    staffcol.delete_many({})
    #for docid in patientcol.view('_all_docs'): #delete all documents in compromised patient section
    patientcol.delete_many({})

    # rocovery from local and store it on cloud server. Open local folder according to leaked section
    
    # patient recover and encrypt
    directory_patient = 'section{}_patient'.format(target_section)

    for filename in os.listdir(directory_patient): #encrypt local patient's documents and upload to MongoDB
        f = os.path.join(directory_patient, filename)
        # checking if it is a file
        if os.path.isfile(f):
            
            #print('patient sec :',target_section)
            
            with open(f, 'rb') as file:
                local_file = file.read()
                data = local_file.decode('ISO-8859-1')
                data = json.loads(data)
            
            with open('section{}-staff.key'.format(target_section),'rb') as file2:
                new_key = file2.read()
            
            doc_string = json.dumps(data)
            #doc_sorted = json.dumps(local_file, indent = 3)
            
            doc_encrypted = symcrytjson.encryptjson(new_key,doc_string,"") 
            #doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
            print("Re-encrypted the patient's documents")
            patientcol = mydb["section{}-patient".format(target_section)]
            patientcol.insert_one(doc_encrypted)
            
    
    # staff recover and encrypt
    directory_staff = 'section{}_staff'.format(target_section)

    for filename in os.listdir(directory_staff): #encrypt local staff's documents and upload to MongoDB
        fs = os.path.join(directory_staff, filename)
        # checking if it is a file
        if os.path.isfile(fs):
            #print(f)
            
            #print('staff sec :',target_section)
            
            with open(f,'rb') as file:
                local_file = file.read()
                data = local_file.decode('ISO-8859-1')
                data = json.loads(data)
            
            with open('section{}-staff.key'.format(target_section),'rb') as file:
                new_key = file.read()
                
            doc_string = json.dumps(data)
            
            doc_encrypted = symcrytjson.encryptjson(new_key,doc_string,"") 
            print("Used key: ",new_key)
            print("Re-encrypted the staff's documents")
            staffcol = mydb["section{}-staff".format(target_section)]
            staffcol.insert_one(doc_encrypted)