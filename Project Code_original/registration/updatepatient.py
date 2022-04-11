
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
import registrar


def updatepatient(key,patientdb):
    couch = couchdb.Server('http://{}:{}@localhost:5984/'.format("nontawat","non123"))
    db = couch[patientdb]   
    #Enter patient name
    while(True):
        while(True):
            pname = input("Enter patient name: ")
            #type "exit" to terminate the program
            if pname == "exit":
                exit()
            elif pname == "back":
                registrar.registrar(key,patientdb)
            wanteddoc = findDoc.findDoc(key,pname,patientdb)

            if wanteddoc != "none": #if function findDoc found the document then break the while loop
                break
        
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        decdoc_sorted = json.dumps(decdoc, indent = 6)
        print("{}'s document: \n{}".format(pname,decdoc_sorted))

        while(True):
            edit_attr = input("Which {}'s attributes do you want to edit? (back->Enter staff name, exit->exit the program):".format(pname))
            if edit_attr in decdoc:
                print("have attr")
                while(True):
                    new_val = input("Enter the new value of attribute {} (back->select attribute, exit->exit the program): ".format(edit_attr))
                    if new_val == "exit":
                        exit()
                    elif new_val=="back":
                        break
                    else:
                        #apply new value to the selected attribute 
                        decdoc[edit_attr] = new_val

                        #covert the edited document to string
                        edited_decdoc_string = json.dumps(decdoc)

                        #encrypt the edited document
                        encrypted_edited_decdoc = symcrytjson.encryptjson(key,edited_decdoc_string)

                        #reindent the edited document
                        edited_decdoc_sorted = json.dumps(decdoc, indent = 6)

                        #reindent the encryted edited document
                        encrypted_edited_decdoc_sorted = json.dumps(encrypted_edited_decdoc, indent = 6)

                        #print the results
                        print("Edited {}'s document: \n{}".format(pname,edited_decdoc_sorted))
                        print("Encrypted edited {}'s document: \n{}".format(pname,encrypted_edited_decdoc_sorted))

                        #update to the database
                        while(True): #If user input the unexpected command then ask again
                            confirm = input("Do you want to save the above encrypted document? (y/n/exit): ")
                            if confirm == "y":
                                try:
                                    db.delete(wanteddoc)
                                    db.save(encrypted_edited_decdoc)
                                    print("The document has been saved to {}".format(db.name))
                                except(couchdb.http.ServerError):
                                    print("Cannot save the document")
                                break
                            elif confirm == "n":
                                break
                            elif confirm == "exit":
                                exit()
                            else:
                                print("Invalid command, please try again")
                        if confirm in ("y","n"):
                            break
            elif edit_attr=="back":
                break
            elif edit_attr == "exit":
                exit()
            else:
                print("Invalid attribute, please try again")
            

#test the function
#updatestaff("hospital_section1")