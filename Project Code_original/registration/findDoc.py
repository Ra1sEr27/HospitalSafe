from cryptography.fernet import Fernet
import onetimepad
import getpass
from pymongo import MongoClient
import pymongo
import hashlib
import hmac
import binascii


def findDoc(key,id,db):

    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client['Hospital']
    mycol = mydb[db]
    id_byte = str.encode(id)
    #generate MAC from patient id
    print("key: {}, id: {}".format(key,id_byte))
    newhmac = hmac.new(key, id_byte, digestmod=hashlib.sha256)
    newmd = newhmac.hexdigest()
    print("MD_id: ",newmd)
    document = mycol.find_one({'MD_id': newmd}) #find the wanted document by MD_id
    return document
