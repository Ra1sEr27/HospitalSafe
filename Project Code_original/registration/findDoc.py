from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii

def findDoc(key,name,db):

    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    db = couch[db]
    name_byte = str.encode(name)
    #generate MAC from patient name
    newhmac = hmac.new(key, name_byte, digestmod=hashlib.sha256)
    newmd = newhmac.hexdigest()
    #Get id from database
    wanteddoc = "none"
    for docid in db.view('_all_docs'): #find the wanted document by comparing MD
        i = docid['id']
        browsedoc = db[i]
        #print(browsedoc)
        origMD_pname = browsedoc['MD_name']
        if origMD_pname == newmd:
            wanteddoc = browsedoc
            break
    # if wanteddoc == "none":
    #     print("The wanted document is not found, please try again")

    return wanteddoc