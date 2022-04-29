from types import NoneType
from cryptography.fernet import Fernet
import onetimepad
import getpass
from pymongo import MongoClient
import pymongo
import json
import hashlib
import hmac
import os
import findDoc
import symcrytjson
import updateadmin
def updateregistrar(key,registrarid):
            wanteddoc = findDoc.findDoc(key,registrarid,"section1_staff")
            section_no=1
            while type(wanteddoc) == NoneType: #find registrar's document in every staff database
                section_no += 1
                if section_no==6:
                    print("There is no {}'s document stored in the system".format(registrarid))
                    break
                wanteddoc = findDoc.findDoc(key,registrarid,"section{}-staff".format(section_no))

            if type(wanteddoc) != NoneType: #Found the wanted document
                decdoc = symcrytjson.decryptjson(key,wanteddoc)
                decdoc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                decdoc_sorted = json.dumps(decdoc_lite,indent = 6)
                print("{}'s document : \n{}".format(registrarid,decdoc_sorted))
                
                while(True):
                    edit_attr = input("Which {}'s attributes do you want to edit? (back->Enter staff name, exit->exit the program):".format(registrarid))
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
                                edited_decdoc_string_sorted = json.dumps(decdoc, indent = 3)
                                #encrypt the edited document
                                encrypted_edited_decdoc = symcrytjson.encryptjson(key,edited_decdoc_string,"")

                                #reindent the edited document
                                edited_decdoc_sorted = json.dumps(decdoc, indent = 3)

                                #reindent the encryted edited document
                                encrypted_edited_decdoc_sorted = json.dumps(encrypted_edited_decdoc, indent = 3)

                                #print the results
                                edited_doc_lite = {"name": "{}".format(decdoc["name"]), "password": "", "role": "{}".format(decdoc["role"]), "accessdb": "{}".format(decdoc["accessdb"])}
                                edited_doc_lite_sorted = json.dumps(edited_doc_lite, indent = 3)
                                print("Edited {}'s document: \n{}".format(registrarid,edited_doc_lite_sorted))
                                print("Encrypted edited {}'s document: \n{}".format(registrarid,encrypted_edited_decdoc_sorted))

                                #update to the database
                                while(True): #If user input the unexpected command then ask again
                                    confirm = input("Do you want to save the above encrypted document? (y/n/exit): ")
                                    if confirm == "y":
                                        try:
                                            client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
                                            db = client['Hospital'] #connect to db
                                            staffcol = db["section{}-staff".format(section_no)]
                                            staffcol.delete_one(wanteddoc)
                                            staffcol.insert_one(encrypted_edited_decdoc)
                                            #delete original local file name
                                            f = open('./section{}_staff/{}_{}.json'.format(section_no,registrarid,origName), 'w') #delete local file
                                            f.close()
                                            os.remove(f.name)
                                            with open('./section{}_staff/{}_{}.json'.format(section_no,registrarid,decdoc["name"]),'w') as file:
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