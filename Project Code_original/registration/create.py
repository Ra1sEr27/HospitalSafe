from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii


def create():
    #code for testing
    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')

    while(True): #keep the program running
        dbname = input("Enter database name : ")
        #type "exit" to terminate the program
        if dbname == "exit":
            exit()
        elif dbname == "back":
            break
        try:
            couch.create(dbname)
            print("Database {} has been created".format(dbname))
        except(couchdb.http.ServerError):
            print("Illegal database name (Only lowercase characters (a-z), digits (0-9), and any of the characters _, $, (, ), +, -, and / are allowed. Must begin with a letter.)")

