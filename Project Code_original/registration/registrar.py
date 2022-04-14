from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import insertpatient
import updatepatient
import deletepatient
import insertadmin_registrar_staff
import deletestaff
import updatestaff
import getalldoc

def registrar(key,accessdb):
    if accessdb in ("db1","hospital_section1","section1_staff"):
        patientdb = "hospital_section1"
        staffdb = "section1_staff"
    elif accessdb in ("db2","hospital_section2","section2_staff"):
        patientdb = "hospital_section2"
        staffdb = "section2_staff"
    elif accessdb in ("db3","hospital_section3","section3_staff"):
        patientdb = "hospital_section3"
        staffdb = "section3_staff"
    elif accessdb in ("db4","hospital_section4","section4_staff"):
        patientdb = "hospital_section4"
        staffdb = "section4_staff"
    elif accessdb in ("db5","hospital_section5","section5_staff"):
        patientdb = "hospital_section5"
        staffdb = "section5_staff"
    else:
        print("Database {} is not existed".format(accessdb))
        return False
    while(True):
        type = input("Which types of document do you want to view/insert/modify? (medical staff,patient,back): ")
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
                command1 = input("Which tasks do you want to do? (view/insert,modify,back): ")
                
                if command1 == "view":
                    getalldoc.getalldoc(key, accessdb)
                elif command1 == "insert":
                    #print("staffdb: ",staffdb)
                    insertadmin_registrar_staff.insertadmin_registrar_staff(key,staffdb,"registrar","medical staff")
                elif command1 == "modify":
                    command = input("What do you want to do with this document? (update,delete,back): ")
                    if command =="update":
                        updatestaff.updatestaff(key,staffdb)
                    elif command =="delete":
                        deletestaff.deletestaff(key,staffdb)
                    elif command =="back": # exit the if-statement
                        break
                    else:
                        print("Invalid command")
                elif command1 == "back":
                    break
                else:
                    print("Invalid command")
        elif type == "back":
            exit()
        else:
            print("Invalid type, please try again")

