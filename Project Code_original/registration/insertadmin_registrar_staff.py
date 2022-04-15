
from struct import pack
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import ast
import symcrytjson
import getpass
import registrar
import admin
def insertadmin_registrar_staff(key,accessdb,inserterrole,role):
    while(True):
        try:
            # connect to the DB
            couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
            
            db= couch[accessdb]
        except(couchdb.http.Unauthorized,couchdb.http.ResourceNotFound):
            print("Database is not existed")
        #print("---Type exit or back to go back to registrar---")
        username = input("Enter name: ")
        if username == "exit":
            exit()
        elif username == "back":
            if inserterrole == "registrar":
                registrar.registrar(key,accessdb)
            elif inserterrole == "admin":
                admin.admin(key,"nontawat")
            else:
                break
        while(True):
            password = getpass.getpass("Enter password: ")
            if password == "exit":
                exit()
            elif password == "back":
                break
            confirmpasswd = getpass.getpass("Enter password again: ")
            if confirmpasswd == "exit":
                exit()
            elif confirmpasswd == "back":
                break
            if password == confirmpasswd:
                break
            else:
                print("Passwords are not matched, please try again")

        # create a json format from input
        doc = {"name": "{}".format(username), "password": "{}".format(password), "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_lite = {"name": "{}".format(username), "password": "", "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_sorted = json.dumps(doc_lite, indent=3)
        print("Document: \n{}".format(doc_sorted))
        # Convert JSON to string
        doc = json.dumps(doc)
        #encrypt the document
        doc_encrypted = symcrytjson.encryptjson(key,doc)
        doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
        print("Encrypted document: \n", doc_encrypted_sorted)
        confirm = input("Do you want to insert the above encrypted document? (y/n/back/exit): ")
        if confirm == "y":
            try:
                db.save(doc_encrypted)
                print("The document has been saved to {}".format(db.name))
            except(couchdb.http.ServerError):
                print("Cannot save the document")
        elif confirm == "n":
            break
        elif confirm == "back":
            pass
        elif confirm == "exit":
            exit()
        else:
            print("Invalid command, please try again")
            
