from cryptography.fernet import Fernet
import os
import couchdb
from pymongo import MongoClient
import pymongo

import keygenerator
def create():
    client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client["Hospital"]
    #get amount of collections
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
        patientcol = "section{}-patient".format(picknum)
        mycol = mydb[patientcol]
        mydict = { "name": "Peter", "address": "Lowstreet 27" }
        x = mycol.insert_one(mydict) #insert doc
        x = mycol.delete_one(mydict)  #delete doc
        print("Database {} has been created".format(patientcol))
        directory = patientcol
        path_dir = os.path.abspath('.') #get current folder directory
        if not os.path.exists(directory): #create folder to path_dir
            os.mkdir(os.path.join(path_dir, directory))

        staffcol = "section{}-staff".format(picknum)
        mycol = mydb[staffcol]
        mydict = { "name": "Peter", "address": "Lowstreet 27" }
        x = mycol.insert_one(mydict) #insert doc
        x = mycol.delete_one(mydict)  #delete doc
        print("Database {} has been created".format(staffcol))
        directory = staffcol
        path_dir = os.path.abspath('.') #get current folder directory
        if not os.path.exists(directory): #create folder to path_dir
            os.mkdir(os.path.join(path_dir, directory))
        
        keygenerator.keygenerator(picknum)
        print("Section {}'s key has been generated".format(picknum))
    except(couchdb.http.ServerError):
        print("Illegal database name (Only lowercase characters (a-z), digits (0-9), and any of the characters _, $, (, ), +, -, and / are allowed. Must begin with a letter.)")
