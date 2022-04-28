from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
from pymongo import MongoClient
import pymongo
import insertadmin_registrar_staff

def create():
    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client["Hospital"]
    while(True): #keep the program running
        colname = input("Enter collection name : ")
        #type "exit" to terminate the program
        if colname == "exit":
            exit()
        elif colname == "back":
            break
        try:
            mycol = mydb[colname]
            mydict = { "name": "Peter", "address": "Lowstreet 27" }
            x = mycol.insert_one(mydict) #insert doc
            x = mycol.delete_one(mydict)  #delete doc
            print("Database {} has been created".format(colname))
        except(couchdb.http.ServerError):
            print("Illegal database name (Only lowercase characters (a-z), digits (0-9), and any of the characters _, $, (, ), +, -, and / are allowed. Must begin with a letter.)")