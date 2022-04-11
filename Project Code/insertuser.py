
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import ast

while(True):
    username = 'nontawat'
    password = 'non123'
    try:
        # connect to the DB
        couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
            
        db = couch['rbac']        
            
        print("Access granted")
        break
    
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")
    
#import key
with open('key.key','rb') as file:
    key = file.read()

    username = input("Enter username : ")
    password = input("Enter password : ")
    role = input('Enter role : ')
    accessdb = input('Enter access database : ')
        
    # create a json format from input
    doc = {"username": "{}".format(username), "password": "{}".format(password), "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
    
    # Serializing json 
    json_object = json.dumps(doc, indent='4')
    
    # Writing to sample.json
    with open("staffinfo.json", "w") as outfile:
        outfile.write(json_object)
    
    print(type(doc))
    doc = '{}'.format(doc)
    print(type(doc))
    doc = str.encode(doc)
    #with open('staffinfo.json','wb') as file:
        #file.write(doc)
    #f = open("staffinfo.json", "w")
    #f.write(str(doc))
    #f.close()
        
    # this opens your json and reads its data into a new variable called 'data'
    with open('staffinfo.json', 'rb') as f:
        data = f.read()
    
    datajson = data.decode('utf8')
    datajson = json.loads(datajson)
    #print(type(datajson))
    #store patient's name in pname variable
    staffname = datajson['username']
    staffpass = datajson['password']

    # convert pname to byte format
    staffname = str.encode(staffname)
    staffpass = str.encode(staffpass)
    staffnamepass = staffname+staffpass
    # this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)

    # create MAC from key and data
    mac = hmac.new(key, data, hashlib.sha256).digest()
    hmac1 = hmac.new(key, staffnamepass, digestmod=hashlib.sha256)
    #Create MD from hmac1
    md1 = hmac1.hexdigest()
    #print(md1)
    #print(type(md1))
    mac = mac.decode('ISO-8859-1')

    # convert bytes to string
    encrypted = encrypted.decode("ISO-8859-1")
    #encpname = encpname.decode("utf-8")

    # Upload ciphertext, MD and MAC to CouchDB
    doc = {'MD_namepass': '{}'.format(staffnamepass), 'CT': '{}'.format(encrypted), 'MAC': '{}'.format(mac)}        

    print("doc: ", doc)
    db.save(doc)

