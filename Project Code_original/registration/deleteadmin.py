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

def deleteadmin(key):
    while(True):
        while(True):
            adminname = input("Enter admin name (type exit to exit the program): ")
            if adminname == "exit":
                exit()
            #find the document
            section_no=0
            while wanteddoc == "none": #find admin's document in every staff database
                section_no += 1
                if section_no==6:
                    print("There is no {}'s document stored in the system".format(adminname))
                    break
                wanteddoc = findDoc.findDoc(key,adminname,"section{}_staff".format(section_no))
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
                        print("{}'s document has been deleted".format(adminname))
                        break
                    elif ans =='n':
                        break
                    elif ans == "exit":
                        exit()
                    else:
                        print("Invalid input, please try again")