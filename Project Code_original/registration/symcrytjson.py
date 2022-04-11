
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii

def encryptjson(key,data_string):

    #convert string to JSON
    data_json = json.loads(data_string)
    #store name in name variable
    name = data_json["name"]
    #convert string to byte for encryption
    data_byte = str.encode(data_string)
    
    # convert pname to byte format
    name_byte = str.encode(name)
    # this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data_byte)
    
    # create MAC from key and data
    mac = hmac.new(key, data_byte, hashlib.sha256).digest()
    hmac1 = hmac.new(key, name_byte, digestmod=hashlib.sha256)
    #Create MD from hmac1
    md1 = hmac1.hexdigest()
    #print(md1)
    #print(type(md1))
    mac = mac.decode('ISO-8859-1')

    # convert bytes to string
    encrypted = encrypted.decode("ISO-8859-1")
    #encpname = encpname.decode("utf-8")

    # Upload ciphertext, MD and MAC to CouchDB
    doc = {'MD_name': '{}'.format(md1), 'CT': '{}'.format(
        encrypted), 'MAC': '{}'.format(mac)}
    #print("doc: ",s)
    #print("Encrypted document: ", doc)
    return doc

def decryptjson(key,doc):
    #store the stored ciphertext in CT
    CT = doc['CT']
    #store the original MAC to origmac
    origmac = doc['MAC']
    #convert string to byte
    CTbytes = str.encode(CT)
    #decrypt the ciphertext
    fernet = Fernet(key)
    decdoc = fernet.decrypt(CTbytes)

    #generate MAC for checking integrity
    mac = hmac.new(key, decdoc, hashlib.sha256).digest()
    mac = mac.decode('ISO-8859-1')

    #convert the decrypted byte to string
    decdoc = decdoc.decode("utf-8")
    #convert string to json format
    decdoc = json.loads(decdoc)
    #reindent the json file
    if mac == origmac:
        print("Integrity checked")
    else:
        print("The data has been modified")
    return decdoc