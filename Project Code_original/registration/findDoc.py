from cryptography.fernet import Fernet
import onetimepad
import getpass
from pymongo import MongoClient
import pymongo
import hashlib
import hmac
import binascii


def findDoc(key,id,db): #WIP

    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
    mydb = client[db]
    id_byte = str.encode(id)
    #generate MAC from patient id
    newhmac = hmac.new(key, id_byte, digestmod=hashlib.sha256)
    newmd = newhmac.hexdigest()
    #Get id from database
    wanteddoc = "none"
    for docid in db.view('_all_docs'): #find the wanted document by comparing MD
        i = docid['id']
        browsedoc = db[i]
        origMD_pid = browsedoc['MD_id']
        if origMD_pid == newmd:
            wanteddoc = browsedoc
            break
    return wanteddoc