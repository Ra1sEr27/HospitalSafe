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
import insertstaff
import deletestaff
import updatestaff


def admin(key):
    while(True):
        type = input("Which types of document do you want to insert/modify? (admin,registrar,back): ")
        if type == "admin":
            while(True):
                command1 = input("Which tasks do you want to do? (insert,modify,back): ")
                if command1 == "insert":
                    insertpatient.insertpatient(key,"admin")
                elif command1 == "modify":
                    command = input("What do you want to do with the document? (update,delete,back): ")
                    if command =="update":
                        updatepatient.updatepatient(key,"admin")
                    elif command =="delete":
                        deletepatient.deletepatient(key,"admin")
                    elif command =="back": # exit the if-statement
                        break
                    else:
                        print("Invalid command")
                elif command1 == "back": # exit the if-statement
                    break
                else:
                    print("Invalid command")
        elif type == "back":
            exit()
        else:
            print("Invalid type, please try again")

