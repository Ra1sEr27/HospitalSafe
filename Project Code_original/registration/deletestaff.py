from cryptography.fernet import Fernet

import json
import hashlib
from pymongo import MongoClient
import pymongo
import findDoc
import symcrytjson
import os
def deletestaff(key,staffdb):
    
    while(True):
        while(True):
            staffid = input("Enter staff id (type exit to exit the program): ")
            if staffid == "exit":
                exit()
            #find the document
            wanteddoc = findDoc.findDoc(key,staffid,staffdb)
            if wanteddoc != "none":
                break

        #decrypt the document
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        
        decdoc_sorted = json.dumps(decdoc, indent = 6)
        print(decdoc_sorted)

        while(True):
            ans = input("Do you want to delete this document? (y/n/exit): ")
            if ans =='y':
                client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
                mydb = client['Hospital'] #connect to db
                mycol = mydb[staffdb] #connect to collection
                mycol.delete_one(wanteddoc)
                f = open('./section{}_patient/{}_{}.json'.format(staffdb[7],staffid,decdoc["name"]), 'w') #delete local file
                f.close()
                os.remove(f.name)
                print("{}'s document has been deleted".format(staffid))
                break
            elif ans =='n':
                break
            elif ans == "exit":
                exit()
            else:
                print("Invalid input, please try again")