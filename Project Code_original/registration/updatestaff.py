
from types import NoneType
from cryptography.fernet import Fernet
import onetimepad
import getpass
import json
from pymongo import MongoClient
import pymongo
import os
import findDoc
import symcrytjson
import registrar
import getpass

def updatestaff(key,staffdb,staffid):

        wanteddoc = findDoc.findDoc(key,staffid,staffdb)
        if type(wanteddoc) == NoneType: #if function findDoc found the document then break the while loop
            print("The document is not existed")
            return 0
            
        decdoc = symcrytjson.decryptjson(key,wanteddoc)
        decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
        decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
        print("{}'s document: \n{}".format(staffid,decdoc_sorted))

        while(True):
            edit_attr = input("Which {}'s attributes do you want to edit? (back->Enter staff name, exit->exit the program):".format(staffid))
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
                        if edit_attr == "name":
                            origName = decdoc["name"]
                        decdoc[edit_attr] = new_val

                        #covert the edited document to string
                        edited_decdoc_string = json.dumps(decdoc)
                        edited_decdoc_string_sorted = json.dumps(decdoc,indent = 3)
                        #encrypt the edited document
                        encrypted_edited_decdoc = symcrytjson.encryptjson(key,edited_decdoc_string,"")

                        #reindent the edited document
                        edited_decdoc_sorted = json.dumps(decdoc, indent = 6)

                        #reindent the encryted edited document
                        encrypted_edited_decdoc_sorted = json.dumps(encrypted_edited_decdoc, indent = 6)

                        #print the results
                        
                        edited_doc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                        print("Edited {}'s document: \n{}".format(staffid,edited_doc_lite))
                        print("Encrypted edited {}'s document: \n{}".format(staffid,encrypted_edited_decdoc_sorted))

                        #update to the database
                        while(True): #If user input the unexpected command then ask again
                            confirm = input("Do you want to save the above encrypted document? (y/n/exit): ")
                            if confirm == "y":
                                try:
                                    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
                                    db = client['Hospital'] #connect to db
                                    staffcol = db[staffdb]
                                    staffcol.delete_one(wanteddoc)
                                    staffcol.insert_one(encrypted_edited_decdoc)
                                    #delete original local file name
                                    f = open('./section{}_staff/{}_{}.json'.format(staffdb[7],staffid,origName), 'w') #delete local file
                                    f.close()
                                    os.remove(f.name)
                                    with open('./section{}_staff/{}_{}.json'.format(staffdb[7],staffid,decdoc["name"]),'w') as file:
                                        file.write(edited_decdoc_string_sorted)
                                    print("The document has been saved to {}".format(staffcol.name))
                                except(pymongo.http.ServerError):
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