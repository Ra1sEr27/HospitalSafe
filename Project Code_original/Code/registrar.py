from types import NoneType
from cryptography.fernet import Fernet

import insertpatient
import updatepatient
import deletepatient
import insertadmin_registrar_staff
import deletestaff
import updatestaff
import getalldoc
import findDoc
def registrar(key,section_no):
    patientdb = "section{}-patient".format(section_no)
    staffdb = "section{}-staff".format(section_no)

    while(True):
        type = input("Which types of document do you want to view/insert/modify? (medical staff,patient,exit): ")
        if type == "patient":
            while(True):
                command1 = input("Which tasks do you want to do? (view,insert,modify,back): ")
                
                if command1 == "view":
                    if command1 == "view":
                        getalldoc.getalldoc(key, patientdb)
                    
                    #getalldoc.getalldoc_views(key, patientdb)
                elif command1 == "insert":
                    insertpatient.insertpatient(key,patientdb)
                elif command1 == "modify":
                    command = input("What do you want to do with the document? (update,delete,back): ")
                    if command =="update":
                        updatepatient.updatepatient(key,patientdb)
                    elif command =="delete":
                        deletepatient.deletepatient(key,patientdb)
                    elif command =="back": # exit the if-statement
                        break
                    else:
                        print("Invalid command")
                elif command1 == "back": # exit the if-statement
                    break
                else:
                    print("Invalid command")
        elif type == "medical staff":
            while(True):
                command1 = input("Which tasks do you want to do? (view,insert,modify,back): ")
                
                if command1 == "view":
                    getalldoc.getalldoc(key, staffdb)
                elif command1 == "insert":
                    insertadmin_registrar_staff.insertadmin_registrar_staff(key,staffdb,"registrar","medical staff")
                elif command1 == "modify":
                    while(True):
                        sid = input("Enter staff's ID (type 'back' to choose the tasks, 'exit' to exit the program): ")
                        if sid == "back":
                            break
                        elif sid == "exit":
                            exit()
                        else:
                            command = input("What do you want to do with this document? (update,delete,back): ")
                            if command =="update":
                                updatestaff.updatestaff(key,staffdb,sid)
                            elif command =="delete":
                                deletestaff.deletestaff(key,staffdb,sid)
                            elif command =="back": # exit the if-statement
                                break
                            else:
                                print("Invalid command")
                elif command1 == "back":
                    break
                else:
                    print("Invalid command")
        elif type == "exit":
            break
        else:
            print("Invalid type, please try again")

