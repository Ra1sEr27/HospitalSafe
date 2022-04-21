from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii

def findDoc(key,id,db):

    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    db = couch[db]
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