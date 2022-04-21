
from struct import pack
from cryptography.fernet import Fernet
import os
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
        #id generator
        if accessdb != "admin": #generate staff id
            section_no = int(accessdb[7])
            if section_no == 1:
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section1_staff'
            elif section_no == 2:
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section2_staff'
            elif section_no == 3:
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section3_staff'
            else:
                print("Invalid section")
            
            staff_no =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]) + 1
            staff_id_first2digits = str(section_no)
            while(len(staff_id_first2digits) != 2):
                staff_id_first2digits = "0" + staff_id_first2digits
            
            staff_id_last4digits = str(staff_no)
            while(len(staff_id_last4digits) != 4):
                staff_id_last4digits = "0" + staff_id_last4digits

            staff_id = role[0] +staff_id_first2digits + staff_id_last4digits
        else: #generate admin id
            dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\admin'
            staff_no =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]) + 1
            staff_id_last4digits = str(staff_no)
            while(len(staff_id_last4digits) != 4):
                staff_id_last4digits = "0" + staff_id_last4digits
            staff_id = "a" + "00" + staff_id_last4digits
        print(staff_id)
        # create a json format from input
        
        doc = {"id": "{}".format(staff_id),"name": "{}".format(username), "password": "{}".format(password), "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_sorted = json.dumps(doc, indent=3)
        doc_lite = {"staffid": "{}".format(staff_id),"name": "{}".format(username), "password": "", "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_lite_sorted = json.dumps(doc_lite, indent=3)
        print("Document: \n{}".format(doc_lite_sorted))
        # Convert JSON to string
        doc = json.dumps(doc)
        #encrypt the document
        doc_encrypted = symcrytjson.encryptjson(key,doc)
        doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
        print("Encrypted document: \n", doc_encrypted_sorted)
        confirm = input("Do you want to insert the above encrypted document? (y/n/back/exit): ")
        if confirm == "y":
            try:
                if role[0] == "a": #save to admin folder
                    with open('./admin/{}_{}.json'.format(staff_id,username),'w') as file:
                        file.write(doc_sorted)
                elif role[0] in ("r","m"): #save to staff folder
                    with open('./admin/{}_{}.json'.format(section_no,staff_id,username),'w') as file:
                        file.write(doc_sorted)
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
            
