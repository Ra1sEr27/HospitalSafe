#this imports the cryptography package
from cryptography.fernet import Fernet
import getpass
import couchdb
import hashlib, hmac, binascii
#username = input("Enter username: ")
#password = getpass.getpass("Enter password: ")
#connect to the DB
#couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
couch = couchdb.Server('http://nontawat:debsirin45063@localhost:5984/')
db = couch['rbac']

#import key
with open('key.key','rb') as file:
    key = file.read()
fernet = Fernet(key)
while(True):
    #Enter patient name
    pname = input("Enter patient name: ")
    #type "exit" to terminate the program
    if pname == "exit":
        break
    #convert patient name from string to byte
    pname = str.encode(pname)
    #generate MAC from patient name
    newhmac = hmac.new(key, pname, digestmod=hashlib.sha256)
    newmd = newhmac.hexdigest()
    #convert MAC in byte to string
    #new_macpn = new_macpn.decode('ISO-8859-1')
    #new_macpn = unicode(new_macpn, "utf-8")

    print("New MD_pname: ",newmd)
    #print(type(newmd))

    #print(encdoc)
    #Get id from database
    wanteddoc = "none"
    for docid in db.view('_all_docs'):
        i = docid['id']
        browsedoc = db[i]
            
        origMD_pname = browsedoc['MD_pname']
        if origMD_pname == newmd:
            wanteddoc = browsedoc
    if wanteddoc == "none":
        print("Cannot find the document")
        exit()
    #id = input("Enter document ID: ")
    #encdoc = db[id]
    CT = wanteddoc['CT']
    origmac = wanteddoc['MAC']

    #convert string to byte
    CTbytes = str.encode(CT)
    #origmac = str.encode(origmac)
    #decrypt the ciphertext
    decdoc = fernet.decrypt(CTbytes)

    #generate MAC for checking integrity
    mac = hmac.new(key, decdoc, hashlib.sha256).digest()
    mac = mac.decode('ISO-8859-1')

    #convert the decrypted byte to string
    decdoc = decdoc.decode("utf-8")
    print(decdoc)
    #print(origMD_pname)
    print("Original MAC: ",origmac)
    print("Created MAC: ",mac)
    if mac == origmac:
        print("Integrity checked")
    else:
        print("The data has been modified")

    if newmd == origMD_pname:
        print("Same MD")

