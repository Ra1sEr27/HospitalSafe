
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
import registrar
import getpass


def updateadmin(key,adminid):
    couch = couchdb.Server('http://{}:{}@localhost:5984/'.format("nontawat","non123"))
    db = couch["admin"]   
    
    wanteddoc = findDoc.findDoc(key,adminid,"admin")

    if wanteddoc != "none": #if function findDoc found the document then break the while loop
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"])}
        decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
        print("{}'s document : \n{}".format(adminid,decdoc_sorted))
        
        while(True):
            edit_attr = input("Which {}'s attributes do you want to edit? (Enter attribute, back, exit):".format(adminid))
            if edit_attr in decdoc:
                while(True):
                    if edit_attr == "password":
                        while(True):
                            new_val = getpass.getpass("Enter the new value of attribute {} (back->select attribute, exit->exit the program): ".format(edit_attr))
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
                    else:
                        new_val = input("Enter the new value of attribute {} (back->select attribute, exit->exit the program): ".format(edit_attr))
                    if new_val == "exit":
                        exit()
                    elif new_val=="back":
                        break
                    
                    
                    if edit_attr != "password" or confirm == new_val:
                        #apply new value to the selected attribute
                        if edit_attr == "name":
                            origName = decdoc["name"] 
                        decdoc[edit_attr] = new_val

                        #for displaying
                        edited_decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"])}
                        #covert the edited document to string and indent
                        edited_decdoc_string = json.dumps(decdoc)
                        edited_decdoc_string_sorted = json.dumps(decdoc, indent = 6)
                        #encrypt the edited document
                        encrypted_edited_decdoc = symcrytjson.encryptjson(key,edited_decdoc_string)

                        #reindent the edited document
                        edited_decdoc_sorted = json.dumps(edited_decdoc_lite, indent = 6)

                        #reindent the encryted edited document
                        encrypted_edited_decdoc_sorted = json.dumps(encrypted_edited_decdoc, indent = 6)

                        #print the results
                        print("Edited {}'s document: \n{}".format(adminid,edited_decdoc_sorted))
                        print("Encrypted edited {}'s document: \n{}".format(adminid,encrypted_edited_decdoc_sorted))

                        #update to the database
                        while(True): #If user input the unexpected command then ask again
                            confirm = input("Do you want to save the above encrypted document? (y/n/exit): ")
                            if confirm == "y":
                                try:
                                    db.delete(wanteddoc)
                                    db.save(encrypted_edited_decdoc)
                                    #delete original local file name
                                    f = open('./admin/{}_{}.json'.format(adminid,origName), 'w') #delete local file
                                    f.close()
                                    os.remove(f.name)
                                    with open('./admin/{}_{}.json'.format(adminid,decdoc["name"]),'w') as file:
                                        file.write(edited_decdoc_string_sorted)
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