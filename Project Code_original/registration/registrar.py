from cryptography.fernet import Fernet

import insertpatient
import updatepatient
import deletepatient
import insertadmin_registrar_staff
import deletestaff
import updatestaff
import getalldoc

def registrar(key,accessdb):
    if accessdb in ("db1","section1-patient","section1-staff"):
        patientdb = "section1-patient"
        staffdb = "section1-staff"
    elif accessdb in ("db2","section-patient2","section2-staff"):
        patientdb = "section2-patient"
        staffdb = "section2-staff"
    elif accessdb in ("db3","section-patient3","section3-staff"):
        patientdb = "section3-patient"
        staffdb = "section3-staff"
    else:
        print("Database {} is not existed".format(accessdb))
        return False
    while(True):
        type = input("Which types of document do you want to view/insert/modify? (medical staff,patient,logout): ")
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
        elif type == "logout":
            break
        else:
            print("Invalid type, please try again")

