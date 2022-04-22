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
import os
def deleteregistrar(key):
    while(True):
        registrarid = input("Enter registrar id (type exit to exit the program): ")
        if registrarid == "exit":
            exit()
        elif registrarid == "back":
            break
        #find the document
        section_no=0
        while(True): #find registrar's document in every staff database
            section_no += 1
            if section_no==6:
                print("There is no {}'s document stored in the system".format(registrarid))
                break
            wanteddoc = findDoc.findDoc(key,registrarid,"section{}_staff".format(section_no))
            if wanteddoc != "none": #found the document
                break
        if wanteddoc != "none":
            #decrypt the document
            decdoc = symcrytjson.decryptjson(key,wanteddoc)
            
            decdoc_sorted = json.dumps(decdoc, indent = 6)
            print(decdoc_sorted)
            while(True):
                ans = input("Do you want to delete this document? (y/n/exit): ")
                if ans =='y':
                    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
                    db1 = couch["section{}_staff".format(section_no)]
                    db1.delete(wanteddoc)
                    f = open('./section{}_patient/{}_{}.json'.format(section_no,registrarid,decdoc["name"]), 'w') #delete local file
                    f.close()
                    os.remove(f.name)
                    print("{}'s document has been deleted".format(registrarid))
                    break
                elif ans =='n':
                    break
                elif ans == "exit":
                    exit()
                else:
                    print("Invalid input, please try again")