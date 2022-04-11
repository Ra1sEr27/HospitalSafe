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

def deletepatient(key,patientdb):
    
    while(True): #keep the program running
        while(True):
            pname = input("Enter patient name: ")
            if pname == "exit":
                exit()
            #find the document
            wanteddoc = findDoc.findDoc(key,pname,patientdb)
            if wanteddoc != "none":
                break
            
        #decrypt the document
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        
        decdoc_sorted = json.dumps(decdoc, indent = 6)
        print(decdoc_sorted)

        while(True): #keep asking for the confirmation
            ans = input("Do you want to delete this document? (y/n/exit): ")
            if ans =='y':
                couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
                db1 = couch[patientdb]
                db1.delete(wanteddoc)
                print("{}'s document has been deleted".format(pname))
                break
            elif ans =='n':
                break
            elif ans == "exit":
                exit()
            else:
                print("Invalid input, please try again")

# with open('key.key', 'rb') as file:
#     key = file.read()
# deletepatient(key,"hospital_section1")
