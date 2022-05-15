from cryptography.fernet import Fernet
import json
import os
import findDoc
import symcrytjson
from pymongo import MongoClient
import pymongo, keyrevocation

def deleteadmin(key,adminid):
    wanteddoc = findDoc.findDoc(key,adminid,"admin")
    if wanteddoc != "none":
        #decrypt the document
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        
        decdoc_sorted = json.dumps(decdoc, indent = 6)
        print(decdoc_sorted)
        while(True):
            ans = input("Do you want to delete this document? (y/n/exit): ")
            if ans =='y':
                client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
                mydb = client['Hospital'] #connect to db
                mycol = mydb['admin']
                mycol.delete_one(wanteddoc)
                f = open('./admin/{}_{}.json'.format(adminid,decdoc["name"]), 'w') #delete local file
                f.close()
                os.remove(f.name)
                print("{}'s document has been deleted".format(adminid))
                keyrevocation.keyrevocation("0")
                return True
            elif ans =='n':
                break
            elif ans == "exit":
                exit()
            else:
                print("Invalid input, please try again")