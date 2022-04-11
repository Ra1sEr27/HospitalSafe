
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii

while(True):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    try:
    # connect to the DB
        couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
        
        db = couch['hospital_section1']
        
        checkauthen()
        
        
        print("Access granted")
        break
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")

# this just opens your 'key.key' and assings the key stored there as 'key'
with open('key.key', 'rb') as file:
    key = file.read()
while(True):
    filename = input("Enter file name: ")
    if filename == "exit":
        break
    # this opens your json and reads its data into a new variable called 'data'
    with open(filename, 'rb') as f:
        data = f.read()
    #convert data to byte format
    datajson = data.decode('utf8')
    datajson = json.loads(datajson)
    print(datajson)
    #store patient's name in pname variable
    pname = datajson["name"]

    # convert pname to byte format
    pname = str.encode(pname)
    # this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    # create MAC from key and data
    mac = hmac.new(key, data, hashlib.sha256).digest()
    hmac1 = hmac.new(key, pname, digestmod=hashlib.sha256)
    #Create MD from hmac1
    md1 = hmac1.hexdigest()
    #print(md1)
    #print(type(md1))
    mac = mac.decode('ISO-8859-1')

    # convert bytes to string
    encrypted = encrypted.decode("ISO-8859-1")
    #encpname = encpname.decode("utf-8")

    # Upload ciphertext, MD and MAC to CouchDB
    doc = {'MD_pname': '{}'.format(md1), 'CT': '{}'.format(
        encrypted), 'MAC': '{}'.format(mac)}
    #print("doc: ",s)
    print("doc: ", doc)
    db.save(doc)

