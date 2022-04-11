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
import updateadmin
def updateregistrar(key):
    while(True):
        while(True):
            registrarname = input("Enter staff name : ")
            if registrarname == "back":
                break
            elif registrarname == "exit":
                exit()
            wanteddoc = findDoc.findDoc(key,registrarname,"section1_staff")
            section_no=0
            while wanteddoc == "none": #find registrar's document in every staff database
                section_no += 1
                if section_no==6:
                    print("There is no {}'s document stored in the system".format(registrarname))
                    break
                wanteddoc = findDoc.findDoc(key,registrarname,"section{}_staff".format(section_no))
            if wanteddoc != "none":
                decdoc = symcrytjson.decryptjson(wanteddoc)
                decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
                
                print("{}'s document : \n{}".format(registrarname,decdoc_sorted))
                
                while(True):
                    edit_attr = input("Which {}'s attributes do you want to edit? (back->Enter staff name, exit->exit the program):".format(registrarname))
                    if edit_attr in decdoc:
                        while(True):
                            if edit_attr != "password":
                                new_val = input("Enter the new value of attribute {} (back->select attribute, exit->exit the program): ".format(edit_attr))
                            else:
                                new_val = getpass.getpass("Enter the new password (back->select attribute, exit->exit the program): ".format(edit_attr))
                                while(True):
                                    confirm = getpass.getpass("Enter your password again : ")
                                    if confirm == "back":
                                        break
                                    elif confirm == "exit":
                                        exit()
                                    elif confirm == new_val:
                                        print("password matched")
                                        break
                                    else:
                                        print("Passwords are not matched, please try again")
                            if new_val == "exit":
                                exit()
                            elif new_val=="back":
                                break

                            if edit_attr != "password" or confirm == new_val:
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
                                print("Edited {}'s document: \n{}".format(registrarname,edited_decdoc_sorted))
                                print("Encrypted edited {}'s document: \n{}".format(registrarname,encrypted_edited_decdoc_sorted))

                                #update to the database
                                while(True): #If user input the unexpected command then ask again
                                    confirm = input("Do you want to save the above encrypted document? (y/n/exit): ")
                                    if confirm == "y":
                                        try:
                                            couch = couchdb.Server('http://{}:{}@localhost:5984/'.format("nontawat","non123"))
                                            db = couch[section_no]
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
    
    
    
