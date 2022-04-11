
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii


username = input("Enter username: ")
password = getpass.getpass("Enter password: ")

# connect to the DB
couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
#couch = couchdb.Server('http://nontawat:debsirin45063@localhost:5984/')
db = couch['rbac']

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

    datajson = data.decode('utf8')
    datajson = json.loads(datajson)
    pname = datajson["name"]

    # convert pname to byte format
    pname = str.encode(pname)
    # print(pname)
    # this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data)
    #encpname = fernet.encrypt(pname)

    # create MAC from key and data
    mac = hmac.new(key, data, hashlib.sha256).digest()
    #macpn = hmac.new(key, pname, hashlib.sha256).digest()

    hmac1 = hmac.new(key, pname, digestmod=hashlib.sha256)
    md1 = hmac1.hexdigest()
    print(md1)
    print(type(md1))
    mac = mac.decode('ISO-8859-1')

    #macpn = unicodedata.normalize('NFKD', macpn).encode('ascii', 'ignore')
    #macpn = macpn.decode('ISO-8859-1')

    # convert bytes to string
    encrypted = encrypted.decode("ISO-8859-1")
    #encpname = encpname.decode("utf-8")
    #otp = onetimepad.encrypt(json.dumps(data), 'random')

    # Upload ciphertext, MD and MAC to CouchDB
    #doc = {'pname':'{}'.format(encpname),'MAC_PN': '{}'.format(macpn),'CT': '{}'.format(encrypted),'MAC': '{}'.format(mac)}
    doc = {'MD_pname': '{}'.format(md1), 'CT': '{}'.format(
        encrypted), 'MAC': '{}'.format(mac)}
    #s = json.dumps(doc, indent=4, sort_keys=False)
    #print("doc: ",s)
    print("doc: ", doc)
    db.save(doc)
    # this writes your new, encrypted data from OTP into a new JSON file
    # with open('OTPencryptedexample.json','wb') as f:
    #    f.write(otp)

    # Decryption part
    # this opens your json and reads its data into a new variable called 'data'
    # with open('encryptedexample.json','rb') as f:
    #    data = f.read()

    # with open('OTPencryptedexample.json','rb') as f:
    #    otpdata = f.read()

    # this decrypts the data read from your json and stores it in 'decrypted'
    #fernet = Fernet(key)
    #decrypted = fernet.decrypt(data)
    #otpmsg = onetimepad.decrypt(otpdata, 'random')

    # this writes your new, decrypted data into a new JSON file
    # with open('decryptedexample.json','wb') as f:
    #    f.write(decrypted)

    # this writes your new, decrypted data into a new JSON file
    # with open('OTPdecryptedexample.json','wb') as f:
    #    f.write(otpmsg)
