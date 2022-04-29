from types import NoneType
from cryptography.fernet import Fernet

import insertadmin_registrar_staff
import updateadmin, deleteadmin
import updateregistrar, deleteregistrar
import create, drop
import getalldoc
import findDoc
def admin(key,adminid):
    while(True):
        sqlcommand = input("Which type SQL commands do you want to use? (DDL,DML,back) : ")
        sqlcommand = sqlcommand.lower()
        if sqlcommand == "ddl":
            while(True):
                type = input("Which type of DDL do you want to do? (create, drop, back, exit) : ")
                type = type.lower()
                if type == "create":
                    create.create()
                elif type == "drop":
                    drop.drop()
                elif type == "back":
                    break
                elif type == "exit":
                    exit()
                else:
                    print("Invalid command, please try again")
        elif sqlcommand == "dml":
            while(True):
                type = input("Which roles of user's document do you want to insert/modify? (admin,registrar,back): ")
                if type == "admin":
                    while(True):
                        command1 = input("Which tasks do you want to do? (view,insert,modify,back): ")
                        if command1 == "insert":
                            insertadmin_registrar_staff.insertadmin_registrar_staff(key,"admin","admin","admin")
                        #elif command1 == "view":
                        elif command1 == "view":
                            getalldoc.getalldoc(key,"admin")
                        elif command1 == "modify":
                            command = input("What do you want to do with the document? (update,delete,back): ")
                            if command =="update":
                                updateadmin.updateadmin(key,adminid)
                            elif command =="delete":
                                deleteadmin.deleteadmin(key,adminid)
                            elif command =="back": # exit the if-statement
                                break
                            else:
                                print("Invalid command")
                        elif command1 == "back": # exit the if-statement
                            break
                        else:
                            print("Invalid command")
                elif type == "registrar":
                    while(True):
                        command1 = input("Which tasks do you want to do? (view,insert,modify,back): ")
                        if command1 in ("view","insert", "modify"):
                            if command1 != "insert":
                                while(True): #get registrar ID and section no.
                                    rid = input("Enter registrar's ID: ")
                                    if section_no == "back":
                                        break
                                    elif section_no == "exit":
                                        exit()
                                    wanteddoc = findDoc.findDoc(key,rid,staffdb)
                                    if type(wanteddoc) == NoneType: #if function findDoc found the document then break the while loop
                                        print("The document does not existed")
                                    else: #found the document
                                        break
                                    section_no = rid[2]
                            elif command1 == "insert":
                                while(True): #get section no.
                                    section_no = input("Enter section number: ")
                                    if section_no in ("1","2","3"):
                                        break
                                    elif section_no == "back":
                                        break
                                    elif section_no == "exit":
                                        exit()
                                    else:
                                        print("Invalid section, please try again")
                            
                            staffdb = "section{}-staff".format(section_no)
                            with open('section{}-staff.key'.format(section_no),'rb') as file: #open key for that section
                                key = file.read()
                                
                            if command1 == "insert":
                                insertadmin_registrar_staff.insertadmin_registrar_staff(key,staffdb,"admin","registrar")
                            elif command1 == "view":
                                result = getalldoc.getalldoc(key,"section{}-staff".format(section_no))
                                if not result:
                                    print("The database has been formatted, due to key leaking")
                            elif command1 == "modify":
                                command = input("What do you want to do with this document? (update,delete,back): ")
                                if command =="update":
                                    updateregistrar.updateregistrar(key,rid)
                                elif command =="delete":
                                    deleteregistrar.deleteregistrar(key,rid)
                                elif command =="back": # exit the if-statement
                                    break
                                else:
                                    print("Invalid command")
                        elif command1 == "back":
                            break
                        else:
                            print("Invalid command")
                elif type == "back":
                    break
                else:
                    print("Invalid type, please try again")
        elif sqlcommand == "back":
            break
        else:
            print("Invalid SQL Command, please try again")
