
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
import registrar
def insertpatient(key,patientdb):
    try:
        # connect to the DB
        couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
        
        db = couch[patientdb] # main
        
        db_views = couch[patientdb+'_views']    # views
        
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")
    while(True):
        while(True):
            while(True):
                name = input("Enter username : ")
                if name == "exit":
                    exit()
                elif name == "back":
                    registrar.registrar(key,patientdb)
                while(True):
                    NationalID = input("Enter National ID : ")
                    if NationalID == "exit":
                        exit()
                    elif NationalID == "back":
                        break
                    while(True):
                        dob = input("Enter data of birth : ")
                        if dob == "exit":
                            exit()
                        elif dob == "back":
                            break
                        while(True):
                            Phonenum = input("Enter phone number :")
                            if Phonenum == "exit":
                                exit()
                            elif Phonenum == "back":
                                break
                            while(True):
                                RelativePhonenum = input("Enter relative phone number : ")
                                if RelativePhonenum == "exit":
                                    exit()
                                elif RelativePhonenum == "back":
                                    break
                                while(True):
                                    nationality = input("Enter nationality : ")
                                    if nationality == "exit":
                                        exit()
                                    elif nationality == "back":
                                        break
                                    while(True):
                                        admissionDate = input("Enter admission date : ")
                                        if admissionDate == "exit":
                                            exit()
                                        elif admissionDate == "back":
                                            break
                                        while(True):
                                            email = input("Enter email : ")
                                            if email == "exit":
                                                exit()
                                            elif email == "back":
                                                break
                                            while(True):
                                                status = input("Enter health status : ")
                                                if status == "exit":
                                                    exit()
                                                elif status == "back":
                                                    break
                                                while(True):
                                                    height = input("Enter height : ")
                                                    if height == "exit":
                                                        exit()
                                                    elif height == "back":
                                                        break
                                                    while(True):
                                                        weight = input("Enter weight : ")
                                                        if weight == "exit":
                                                            exit()
                                                        elif weight == "back":
                                                            break
                                                        while(True):
                                                            bloodtype = input("Enter bloodtype : ")
                                                            if bloodtype == "exit":
                                                                exit()
                                                            elif bloodtype == "back":
                                                                break
                                                            doc = {"name":"{}".format(name),
                                                            "NationalID":"{}".format(NationalID),
                                                            "dob":"{}".format(dob),
                                                            "Phonenum":"{}".format(Phonenum), 
                                                            "RelativePhonenum": "{}".format(RelativePhonenum),
                                                            "nationality":"{}".format(nationality),
                                                            "admissionDate": "{}".format(admissionDate),
                                                            "email": "{}".format(email),
                                                            "status": "{}".format(status),
                                                            "height": "{}".format(height),
                                                            "weight":"{}".format(weight),
                                                            "bloodtype":"{}".format(bloodtype)}
                                                            
                                                            
                                                            doc_views = {"name":"{}".format(name),
                                                            "dob":"{}".format(dob),
                                                            "RelativePhonenum": "{}".format(RelativePhonenum),
                                                            "nationality":"{}".format(nationality),
                                                            "status": "{}".format(status),
                                                            "height": "{}".format(height),
                                                            "weight":"{}".format(weight),
                                                            "bloodtype":"{}".format(bloodtype)}

                                                            #covert JSON to string
                                                            doc_string = json.dumps(doc)
                                                            doc_sorted = json.dumps(doc, indent = 3)
                                                            print("Document: \n", doc_sorted)
                                                            
                                                            # docs for views
                                                            doc_string_views = json.dumps(doc_views)
                                                            doc_sorted_views = json.dumps(doc_views, indent = 3)
                                                            print("Document: \n", doc_sorted_views)

                                                            #encrypt the document
                                                            doc_encrypted = symcrytjson.encryptjson(key,doc_string) 
                                                            doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
                                                            
                                                            
                                                            # docs for views
                                                            doc_encrypted_views = symcrytjson.encryptjson(key,doc_string_views) 
                                                            doc_encrypted_sorted_views = json.dumps(doc_encrypted_views, indent = 3)
                                                            
                                                            print("Encrypted view document: \n", doc_encrypted_sorted_views)
                                                            print("Encrypted document: \n", doc_encrypted_sorted)
                                                            
                                                            while(True):
                                                                confirm = input("Do you want to insert the above encrypted document? (y/n/exit): ")
                                                                if confirm == "y":
                                                                    try:
                                                                        # main database
                                                                        db.save(doc_encrypted)
                                                                        
                                                                        # views database
                                                                        db_views.save(doc_encrypted_views)
                                                                        
                                                                        print("The document has been saved to {}".format(db.name))
                                                                        print("The document has been saved to {}".format(db_views.name))
                                                                    except(couchdb.http.ServerError):
                                                                        print("Cannot save the document")
                                                                    insertpatient(key,patientdb) #go back to the top
                                                                elif confirm == "n":
                                                                    insertpatient(key,patientdb) #go back to the top
                                                                elif confirm == "exit":
                                                                    exit()
                                                                else:
                                                                    print("Invalid command, please try again")
            

    # name = "Jill Lundberg"
    # NationalID = "11355-19735-49-0"
    # dob = "April 10, 1956"
    # Phonenum ="847-696-0874"
    # RelativePhonenum = "093-293-2920"
    # nationality = "American"
    # admissionDate = "January 31, 2022"
    # email = "JillLun@gmailcom"
    # status = "Critical"
    # height = 159
    # weight = 66
    # bloodtype = "A+"

            # create a json format from input
            
        
        

# with open('key.key', 'rb') as file:
#     key = file.read()
# insertpatient(key,"hospital_section1")

