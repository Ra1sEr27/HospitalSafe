from cryptography.fernet import Fernet
import onetimepad
import os
import couchdb
from pymongo import MongoClient
import pymongo
import insertadmin_registrar_staff

def create():
    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client["Hospital"]
    while(True): #keep the program running
        coltype = input("Enter collection type (patient/staff) : ")
        #type "exit" to terminate the program
        if coltype == "exit":
            exit()
        elif coltype == "back":
            break
        elif coltype in ("patient","staff"):
            #get amount of staff's collections
            staffcolnumlist = []
            allcollist = mydb.list_collection_names()
            for i in range(len(allcollist)):
                if "staff" in allcollist[i]:
                    staffcolnumlist.append(allcollist[i][7])
            sorted_staffcolnumlist = []
            for i in range(len(staffcolnumlist)):
                sorted_staffcolnumlist.append(int(staffcolnumlist[i]))
            sorted_staffcolnumlist.sort()
            picknum = len(sorted_staffcolnumlist) + 1 #default val of picknum
            i=0
            while(True):
                try:
                    front = sorted_staffcolnumlist[i]
                    back = sorted_staffcolnumlist[i+1]
                    if back-front > 1:
                        picknum = front + 1
                        break
                    i+=1
                except(IndexError):
                    break
            try:
                colname = "section{}-{}".format(picknum,coltype)
                mycol = mydb[colname]
                mydict = { "name": "Peter", "address": "Lowstreet 27" }
                x = mycol.insert_one(mydict) #insert doc
                x = mycol.delete_one(mydict)  #delete doc
                print("Database {} has been created".format(colname))
                directory = colname
                path_dir = "C:/Users/exia4/OneDrive/Desktop/SIIT/Third Year/Second Semester/Network Security/Project/Security-and-Cloud-Project/Project Code_original/registration/"
                if not os.path.exists(directory):
                    os.mkdir(os.path.join(path_dir, directory))
            except(couchdb.http.ServerError):
                print("Illegal database name (Only lowercase characters (a-z), digits (0-9), and any of the characters _, $, (, ), +, -, and / are allowed. Must begin with a letter.)")
        else:
            print("Invalid collection type")
