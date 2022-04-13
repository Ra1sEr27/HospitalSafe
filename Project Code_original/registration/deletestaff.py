from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import findDoc
import symcrytjson

def deletestaff(key,staffdb):
    
    while(True):
        while(True):
            staffname = input("Enter staff name (type exit to exit the program): ")
            if staffname == "exit":
                exit()
            #find the document
            wanteddoc = findDoc.findDoc(key,staffname,staffdb)
            if wanteddoc != "none":
                break

        #decrypt the document
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        
        decdoc_sorted = json.dumps(decdoc, indent = 6)
        print(decdoc_sorted)

        while(True):
            ans = input("Do you want to delete this document? (y/n/exit): ")
            if ans =='y':
                couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
                db1 = couch[staffdb]
                db1.delete(wanteddoc)
                print("{}'s document has been deleted".format(staffname))
                break
            elif ans =='n':
                break
            elif ans == "exit":
                exit()
            else:
                print("Invalid input, please try again")