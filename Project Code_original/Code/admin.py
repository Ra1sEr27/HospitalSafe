from types import NoneType
from cryptography.fernet import Fernet
import pymongo
import insertadmin_registrar_staff
import updateadmin, deleteadmin
import updateregistrar, deleteregistrar
import create, drop
import getalldoc
import findDoc

def admin(key,adminid):
    client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client["Hospital"]
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
                        elif command1 == "view":
                            getalldoc.getalldoc(key,"admin")
                        elif command1 == "modify":
                            command = input("What do you want to do with the document? (update,delete,back): ")
                            if command =="update":
                                updateadmin.updateadmin(key,adminid)
                            elif command =="delete":
                                delconfirm = deleteadmin.deleteadmin(key,adminid)
                                if delconfirm:
                                    return 0
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
                            if command1 not in ("insert","view"):
                                while(True): #get registrar ID and section no.
                                    rid = input("Enter registrar's ID: ")
                                    section_no = rid[2]
                                    if rid== "back":
                                        break
                                    elif rid == "exit":
                                        exit()
                                    staffdb = "section{}-staff".format(rid[2])
                                    with open('{}.key'.format(staffdb),'rb') as file: #open key for that section
                                        key = file.read()
                                    wanteddoc = findDoc.findDoc(key,rid,staffdb)
                                    
                                    if wanteddoc != NoneType: #if function findDoc found the document then break the while loop
                                        break
                                    else: #found the document
                                        print("The document does not existed")
                            elif command1 in ("insert","view"):
                                #get the available section
                                staffcolnumlist = []
                                allcollist = mydb.list_collection_names()
                                for i in range(len(allcollist)):
                                    if "staff" in allcollist[i]:
                                        staffcolnumlist.append(allcollist[i][7])
                                sorted_staffcolnumlist = []
                                for i in range(len(staffcolnumlist)):
                                    sorted_staffcolnumlist.append(int(staffcolnumlist[i]))
                                sorted_staffcolnumlist.sort()
                                while(True): #check inputted section no.
                                    section_no = input("Enter section number {}: ".format(sorted_staffcolnumlist)) #ask for section number
                                    if section_no in staffcolnumlist:
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
                                    updateregistrar.updateregistrar(key,wanteddoc)
                                elif command =="delete":
                                    deleteregistrar.deleteregistrar(key,wanteddoc)
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
