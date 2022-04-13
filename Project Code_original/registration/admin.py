from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import insertadmin_registrar_staff
import updateadmin, deleteadmin
import updateregistrar, deleteregistrar
import create, drop

def admin(key,adminname):
    while(True):
        sqlcommand = input("Which type SQL commands do you want to use? (DDL,DML) : ")
        sqlcommand = sqlcommand.lower()
        if sqlcommand == "ddl":
            while(True):
                type = input("Which type of DDL do you want to do? (create, drop) : ")
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
                    print("Invalid commandm, please try again")
        elif sqlcommand == "dml":
            while(True):
                type = input("Which roles of user's document do you want to insert/modify? (admin,registrar,back): ")
                if type == "admin":
                    while(True):
                        command1 = input("Which tasks do you want to do? (insert,modify,back): ")
                        if command1 == "insert":
                            insertadmin_registrar_staff.insertadmin_registrar_staff(key,"admin","admin")
                        elif command1 == "modify":
                            command = input("What do you want to do with the document? (update,delete,back): ")
                            if command =="update":
                                updateadmin.updateadmin(key,adminname)
                            elif command =="delete":
                                deleteadmin.deleteadmin(key,adminname)
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
                        command1 = input("Which tasks do you want to do? (insert,modify,back): ")
                        if command1 in ("insert", "modify"):
                            while(True):
                                section_no = input("Enter section number (1-5): ")
                                if section_no in ("1","2","3","4","5"):
                                    staffdb = "section{}_staff".format(section_no)
                                    break
                                else:
                                    print("Invalid section, please try again")
                            if command1 == "insert":
                                insertadmin_registrar_staff.insertadmin_registrar_staff(key,staffdb,"registrar")
                            elif command1 == "modify":
                                command = input("What do you want to do with this document? (update,delete,back): ")
                                if command =="update":
                                    updateregistrar.updateregistrar(key)
                                elif command =="delete":
                                    deleteregistrar.deleteregistrar(key,staffdb)
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
        else:
            print("Invalid SQL Command, please try again")
# with open('admin.key', 'rb') as file:
#     key = file.read()
# admin(key)