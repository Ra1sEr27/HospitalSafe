from cryptography.fernet import Fernet
import onetimepad
import getpass
from pymongo import MongoClient
import pymongo
import hashlib
import hmac
import binascii


def findDoc(key,id,db):
    
    client = pymongo.MongoClient("mongodb+srv://Nattapol:satang2000@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client['Hospital']
    mycol = mydb[db]
    id_byte = str.encode(id)
    #generate MAC from patient id
    #print("key: {}, id: {}".format(key,id_byte))
    newhmac = hmac.new(key, id_byte, digestmod=hashlib.sha256)
    newmd = newhmac.hexdigest()
    #print("MD_id: ",newmd)
    try:
        document = mycol.find_one({'MD_id': newmd}) #find the wanted document by MD_id
        #print(document)
    except(pymongo.errors.ServerSelectionTimeoutError):
        print("Connection timeout")
        exit()
    return document
