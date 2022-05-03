
from cryptography.fernet import Fernet
import cryptography
import onetimepad
import getpass
import timeit
import json
import hashlib
import hmac
import binascii
import keyrevocation
def encryptjson(key,data_string,oldkey):
    start = timeit.default_timer()
    #convert string to JSON
    data_json = json.loads(data_string)
    #store name in name variable
    id = data_json["id"]
    #convert string to byte for encryption
    data_byte = str.encode(data_string)
    
    # convert pname to byte format
    id_byte = str.encode(id)
    # this encrypts the data read from your json and stores it in 'encrypted'
    fernet = Fernet(key)
    encrypted = fernet.encrypt(data_byte)
    
    # create MAC from key and data
    mac = hmac.new(key, data_byte, hashlib.sha256).digest()
    #print("key: {}, id: {}".format(key,id_byte))
    hmac1 = hmac.new(key, id_byte, digestmod=hashlib.sha256)
    #Create MD from hmac1
    md1 = hmac1.hexdigest()

    mac = mac.decode('ISO-8859-1')

    # convert bytes to string
    encrypted = encrypted.decode("ISO-8859-1")
    #encpname = encpname.decode("utf-8")

    # Upload ciphertext, MD and MAC to MongoDB
    doc = {'MD_id': '{}'.format(md1), 'CT': '{}'.format(
        encrypted), 'MAC': '{}'.format(mac)}
    stop = timeit.default_timer()
    print('Enc Time: ', stop - start)
    return doc

def decryptjson(key,doc):
    #start = timeit.default_timer()
    #store the stored ciphertext in CT
    #print(doc)
    try:
        CT = doc['CT']
    except(TypeError):
        print("Cannot find the document")
        return False
    #store the original MAC to origmac
    origmac = doc['MAC']
    #convert string to byte
    CTbytes = str.encode(CT)
    #decrypt the ciphertext
    
    with open('admin.key','rb') as file:
        check_key = file.read()
        
    i = 0
    while(key != check_key):
        i+=1
        with open('section{}-staff.key'.format(i),'rb') as file:
            
            check_key = file.read()
    fernet = Fernet(check_key)
    try:
        decdoc = fernet.decrypt(CTbytes)
    except(cryptography.fernet.InvalidToken or cryptography.exceptions.InvalidSignature): 
        print("The data has been modified")
        print("Detected from section: ",str(i))
        keyrevocation.keyrevocation(str(i))
        return False

    #generate MAC for checking integrity
    mac = hmac.new(key, decdoc, hashlib.sha256).digest()
    mac = mac.decode('ISO-8859-1')
    
    #convert the decrypted byte to string
    decdoc = decdoc.decode("utf-8")
    
    #convert string to json format
    decdoc = json.loads(decdoc)
    
    #stop = timeit.default_timer()
    #print('Dec Time: ', stop - start)
    return decdoc
    