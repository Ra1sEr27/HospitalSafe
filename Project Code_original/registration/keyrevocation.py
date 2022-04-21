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
    
def keyrevocation(target_section):
    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    while(True):
        #target_section = input("Enter the compromised section (0-3) : ")
        if target_section == "0":   #target section = admin section
            keygenerator.re_adminkeygenerator()
            db = couch["admin"]
            break
        elif target_section in ("1","2","3"):
            keygenerator.re_staffkeygenerator(target_section)
            staffdb = couch["section{}_staff".format(target_section)]
            patientdb = couch["hospital_section{}".format(target_section)]
            break
        else:
            print("Invalid section, please try again")
            break
    for docid in staffdb.view('_all_docs'): #delete all documents in compromised staff section
        i = docid['id']
        browsedoc = staffdb[i]
        staffdb.delete(browsedoc)

    for docid in patientdb.view('_all_docs'): #delete all documents in compromised patient section
        i = docid['id']
        browsedoc = patientdb[i]
        patientdb.delete(browsedoc)
        
        
    # rocovery from local and store it on cloud server. Open local folder according to leaked section
    if(target_section == "1"):
        
        # patient recover and encrypt
        directory_patient = 'patient_section1'
    
        for filename in os.listdir(directory_patient):
            f = os.path.join(directory_patient, filename)
            # checking if it is a file
            if os.path.isfile(f):
                #print(f)
                
                with open(f,'rb') as file:
                    local_file = file.read()
                
                with open('section{}_staff.key'.format(target_section),'rb') as file:
                    new_key = file.read()
                
                doc_string = json.dumps(local_file)
                doc_sorted = json.dumps(local_file, indent = 3)
                
                doc_encrypted = symcrytjson.encryptjson(new_key,doc_string) 
                doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
                
                db = couch["hospital_section1"]
                db.save(doc_encrypted)
        
        # staff recover and encrypt
        directory_staff = 'section1_staff'
    
        for filename in os.listdir(directory_staff):
            fs = os.path.join(directory_staff, filename)
            # checking if it is a file
            if os.path.isfile(fs):
                #print(f)
                
                with open(f,'rb') as file:
                    local_file = file.read()
                
                with open('section{}_staff.key'.format(target_section),'rb') as file:
                    new_key = file.read()
                    
                doc_string = json.dumps(local_file)
                doc_sorted = json.dumps(local_file, indent = 3)
                
                
                doc_encrypted = symcrytjson.encryptjson(new_key,doc_string) 
                doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
                
                db = couch["section1_staff"]
                db.save(doc_encrypted)