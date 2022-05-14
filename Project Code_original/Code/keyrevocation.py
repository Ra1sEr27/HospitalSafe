from asyncore import write
import keygenerator
from cryptography.fernet import Fernet
from pymongo import MongoClient
import pymongo
import json
import os
import symcrytjson, timeit

def keyrevocation(target_section):
    #start = timeit.default_timer()
    client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
    mydb = client['Hospital']
    
    staffcolnumlist = []
    allcollist = mydb.list_collection_names()
    for i in range(len(allcollist)):
        if "staff" in allcollist[i]:
            staffcolnumlist.append(allcollist[i][7])
    
    if target_section == "0":   #target section = admin section
        with open('admin.key','r') as file:
            old_key = file.read() #keep the old key for authentication MD
        with open('KVL.json','r+') as json_file: #store the old key to KVL
            kvl = json.load(json_file)
        
            if target_section not in kvl:
                entry = {target_section: old_key}
                kvl.update(entry)
            else:
                kvl[target_section] = old_key
            #print(kvl)
            json_file.seek(0)
            json.dump(kvl, json_file)
        keygenerator.re_adminkeygenerator()
        db = mydb["admin"]
        
    elif target_section in staffcolnumlist:
        with open('section{}-staff.key'.format(target_section),'r') as file2:
            old_key = file2.read() #keep the old key for generating MD

        with open('KVL.json','r+') as json_file:#store the old key to KVL
            kvl = json.load(json_file)
        
            if target_section not in kvl:
                entry = {target_section: old_key}
                kvl.update(entry)
            else:
                kvl[target_section] = old_key
            #print(kvl)
            json_file.seek(0)
            json.dump(kvl, json_file)
        keygenerator.re_staffkeygenerator(target_section)
        staffcol = mydb["section{}-staff".format(target_section)]
        patientcol = mydb["section{}-patient".format(target_section)]
        
    else:
        print("Invalid section, please try again")
        exit()
    #for docid in staffcol.find(): #delete all documents in compromised staff section
    staffcol.delete_many({})
    #for docid in patientcol.view('_all_docs'): #delete all documents in compromised patient section
    patientcol.delete_many({})
    
    # re-encryptf patient's document recover
    directory_patient = 'section{}-patient'.format(target_section)

    for filename in os.listdir(directory_patient): #encrypt local patient's documents and upload to MongoDB
        f = os.path.join(directory_patient, filename)
        # checking if it is a file
        if os.path.isfile(f):
            with open(f, 'rb') as file:
                local_file = file.read()
                data_string = local_file.decode('ISO-8859-1')
                #data = json.loads(data)
            
            with open('section{}-staff.key'.format(target_section),'rb') as file2:
                new_key = file2.read()

            doc_encrypted = symcrytjson.encryptjson(new_key,data_string,"") 
            print("Finished re-encryption of patient's documents")
            patientcol = mydb["section{}-patient".format(target_section)]
            patientcol.insert_one(doc_encrypted)
            
    
    # staff recover and encrypt
    directory_staff = 'section{}-staff'.format(target_section)

    for filename in os.listdir(directory_staff): #encrypt local staff's documents and upload to MongoDB
        fs = os.path.join(directory_staff, filename)
        # checking if it is a file
        if os.path.isfile(fs):
            
            with open(fs,'rb') as file:
                local_file = file.read()
                data_string = local_file.decode('ISO-8859-1')
                
            with open('section{}-staff.key'.format(target_section),'rb') as file:
                new_key = file.read()

            #print("staff's data: ",data_string)
            #print("Used key: ",new_key)
            doc_encrypted = symcrytjson.encryptjson(new_key,data_string,"") 
            print("Finished re-encryption of staff's documents")
            
            staffcol = mydb["section{}-staff".format(target_section)]
            staffcol.insert_one(doc_encrypted)
    #stop = timeit.default_timer()
    #print('Time: ', stop - start)