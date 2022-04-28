
from struct import pack
from cryptography.fernet import Fernet
import os
import getpass
import couchdb
from pymongo import MongoClient
import pymongo
import json
import hashlib
import hmac
import timeit
import binascii
import ast
import symcrytjson
import getpass
import registrar
import admin

def insertadmin_registrar_staff(key,accessdb,inserterrole,role):
    while(True):
        try:
            client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")

            mydb = client["Hospital"]
            mycol = mydb[accessdb]
            # connect to the DB
            #couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
            
            #db= couch[accessdb]
        except(couchdb.http.Unauthorized,couchdb.http.ResourceNotFound):
            print("Database is not existed")
        #print("---Type exit or back to go back to registrar---")
        username = input("Enter name: ")
        if username == "exit":
            exit()
        elif username == "back":
            break
        while(True):
            password = getpass.getpass("Enter password: ")
            if password == "exit":
                exit()
            elif password == "back":
                break
            confirmpasswd = getpass.getpass("Enter password again: ")
            if confirmpasswd == "exit":
                exit()
            elif confirmpasswd == "back":
                break
            if password == confirmpasswd:
                break
            else:
                print("Passwords are not matched, please try again")
        #id generator
        #print(accessdb)
        #generate last 4 digit of id
        
        if accessdb != "admin": #generate staff id
            
            section_no = accessdb[7]
            if section_no == "1":
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section1_staff'
            elif section_no == "2":
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section2_staff'
            elif section_no == "3":
                dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section3_staff'
            else:
                print("Invalid section")
            
            #staff_no =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]) + 1
            staff_id_first2digits = str(section_no)
            while(len(staff_id_first2digits) != 2):
                staff_id_first2digits = "0" + staff_id_first2digits
            
            staff_id_last4digits = 0
            staff_id = role[0] +staff_id_first2digits + "000" + str(staff_id_last4digits)
            dir_list = os.listdir(dir_path)
            dir_list_onlyID = []
            for i in range(len(dir_list)): #append all of the file names from the chosen folder
                dir_list_onlyID.append(dir_list[i][:7])
            #print(dir_list_onlyID)
            while(staff_id in dir_list_onlyID): #increase the number of last 4 digits
                staff_id_last4digits = int(staff_id_last4digits)
                staff_id_last4digits += 1
                staff_id_last4digits = str(staff_id_last4digits)
                
                while(len(staff_id_last4digits) != 4): #pad 0 to the left of last 4 digits
                    staff_id_last4digits = "0" + staff_id_last4digits
                    #print("in loop ",staff_id_last4digits)
                staff_id = role[0] +staff_id_first2digits + str(staff_id_last4digits)
        else: #generate admin id
            dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\admin'
            #staff_no =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]) + 1
            staff_id_last4digits = 0
            staff_id = "a000000"
            dir_list = os.listdir(dir_path)
            dir_list_onlyID = []
            for i in range(len(dir_list)):
                dir_list_onlyID.append(dir_list[i][:7])
            #print(dir_list_onlyID)
            while(staff_id in dir_list_onlyID):
                staff_id_last4digits = int(staff_id_last4digits)
                staff_id_last4digits += 1
                staff_id_last4digits = str(staff_id_last4digits)
                while(len(staff_id_last4digits) != 4):
                    staff_id_last4digits = "0" + staff_id_last4digits
                staff_id = "a" + "00" + staff_id_last4digits
        #print(staff_id)
        # create a json format from input
        
        doc = {"id": "{}".format(staff_id),"name": "{}".format(username), "password": "{}".format(password), "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_sorted = json.dumps(doc, indent=3)
        doc_lite = {"id": "{}".format(staff_id),"name": "{}".format(username), "password": "", "role": "{}".format(role), "accessdb": "{}".format(accessdb)}
        doc_lite_sorted = json.dumps(doc_lite, indent=3)
        print("Document: \n{}".format(doc_lite_sorted))
        # Convert JSON to string
        doc = json.dumps(doc)
        #encrypt the document
        start = timeit.default_timer()
        doc_encrypted = encryptjson(key,doc,"")
        stop = timeit.default_timer()
        print('Time: ', stop - start)
        doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
        print("Encrypted document: \n", doc_encrypted_sorted)
        confirm = input("Do you want to insert the above encrypted document? (y/n/back/exit): ")
        if confirm == "y":
            try:
                if staff_id[0] == "a": #save to admin folder
                    with open('./admin/{}_{}.json'.format(staff_id,username),'w') as file:
                        file.write(doc_sorted)
                elif staff_id[0] in ("r","m"): #save to staff folder
                    with open('./section{}_staff/{}_{}.json'.format(section_no,staff_id,username),'w') as file:
                        file.write(doc_sorted)

                x = mycol.insert_one(doc_encrypted)
                print("The document has been saved to {} (id: {}).".format(accessdb,x.inserted_id))
            except(couchdb.http.ServerError):
                print("Cannot save the document")
        elif confirm == "n":
            break
        elif confirm == "back":
            pass
        elif confirm == "exit":
            exit()
        else:
            print("Invalid command, please try again")

def encryptjson(key,data_string,oldkey):
    print("Used key: ",key)
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
    print("key: {}, id: {}".format(key,id_byte))
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
    doc_string = json.dumps(doc)
    doc_byte = str.encode(doc_string)
    # version = '0x80'
    # iv = os.urandom(128) 
    # iv = iv.decode('ISO-8859-1')
    # timestamp = fernet.encrypt_at_time(doc_byte, int(time.time())) 
    # timestamp = timestamp.decode('ISO-8859-1')
    # print(hmac1)
    # print("Version : ",type(version))
    # print("Timestamp : ",type(timestamp))
    # print("IV : ",type(iv))
    # print("CT : ",type(encrypted))
    # print("HMAC : ",type(hmac1))
    
    # print("Version: ",version)
    # print("\n")
    # print("Timestamp: ",timestamp)
    # print("\n")
    # print("IV: ",iv)
    # print("\n")
    # print("Ciphertext: ",encrypted)
    # print("\n")
    # print("HMAC: ",hmac1)
    #print(hmac1)
        
    return doc
    
# with open('admin.key', 'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
#     admin_key = file.read()
# insertadmin_registrar_staff(admin_key,"admin","inserterrole","admin")