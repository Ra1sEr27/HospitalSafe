from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
from pymongo import MongoClient
import pymongo
import symcrytjson

def getalldoc(key,db):

    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
    mydb = client[db]
    #Get id from database
    for docid in mydb.view('_all_docs'): #find the wanted document by comparing MD
        i = docid['id']
        browsedoc = mydb[i]
        if "MD_id" in browsedoc:
            decdoc = symcrytjson.decryptjson(key,browsedoc)
            if not decdoc:  #if decryptjson returned False then terminate this function
                return False
            decdoc_sorted = json.dumps(decdoc,indent = 6)
            if "password" in decdoc:
                decdoc_lite = {"id": "{}".format(decdoc["id"]),"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
            
            #if(decdoc_sorted['password'] != ''):
            #    decdoc['password'] = ''
            print("{}'s document: \n{}".format(decdoc["name"],decdoc_sorted))
        
    return True
