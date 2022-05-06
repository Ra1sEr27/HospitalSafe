from types import NoneType
from cryptography.fernet import Fernet
import json
import keyrevocation
from pymongo import MongoClient
import pymongo
import findDoc
import symcrytjson
import os
def deletestaff(key,staffdb,staffid):
    wanteddoc = findDoc.findDoc(key,staffid,staffdb)
    if type(wanteddoc) == NoneType: #the document is existed
        print("The document is not existed")
        return 0
    #decrypt the document
    decdoc = symcrytjson.decryptjson(key,wanteddoc)


    decdoc_sorted = json.dumps(decdoc, indent = 6)
    print(decdoc_sorted)

    while(True):
        ans = input("Do you want to delete this document? (y/n/exit): ")
        if ans =='y':
            client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
            mydb = client['Hospital'] #connect to db
            mycol = mydb[staffdb] #connect to collection
            mycol.delete_one(wanteddoc)
            f = open('./section{}-staff/{}_{}.json'.format(staffdb[7],staffid,decdoc["name"]), 'w') #delete local file
            f.close()
            os.remove(f.name)
            print("{}'s document has been deleted".format(staffid))
            keyrevocation.keyrevocation(decdoc["id"][2])
            break
        elif ans =='n':
            break
        elif ans == "exit":
            exit()
        else:
            print("Invalid input, please try again")