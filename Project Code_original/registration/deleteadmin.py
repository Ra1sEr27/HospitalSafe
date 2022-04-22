from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import os
import findDoc
import symcrytjson

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
                couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
                db1 = couch["admin"]
                db1.delete(wanteddoc)
                f = open('./admin/{}_{}.json'.format(adminid,decdoc["name"]), 'w') #delete local file
                f.close()
                os.remove(f.name)
                print("{}'s document has been deleted".format(adminid))
                break
            elif ans =='n':
                break
            elif ans == "exit":
                exit()
            else:
                print("Invalid input, please try again")