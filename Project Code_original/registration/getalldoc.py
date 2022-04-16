from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import symcrytjson

def getalldoc(key,db):

    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    db1 = couch[db]
    #Get id from database
    for docid in db1.view('_all_docs'): #find the wanted document by comparing MD
        i = docid['id']
        browsedoc = db1[i]
        if "MD_name" in browsedoc:
            decdoc = symcrytjson.decryptjson(key,browsedoc)
            if not decdoc:  #if decryptjson returned False then terminate this function
                return False
            decdoc_sorted = json.dumps(decdoc,indent = 6)
            if "password" in decdoc:
                decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
            
            #if(decdoc_sorted['password'] != ''):
            #    decdoc['password'] = ''
            print("{}'s document: \n{}".format(decdoc["name"],decdoc_sorted))
        
    return True
