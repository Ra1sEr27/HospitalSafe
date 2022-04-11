from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import registrar
import create 
import drop
import findDoc
import symcrytjson
import getpass
import view
import admin
def index():
    while(True):
        username = 'nontawat'
        password = 'non123'
        try:
            # connect to the DB
            couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
                
            #db = couch['rbac']        
                
            print("Access granted")
            break
        
        except(couchdb.http.Unauthorized):
            print("Invalid username or password")

    while(True):
        username = input("please insert username : ")
        password = getpass.getpass("please insert password : ")
        accessdb = input("section : ")
        #add exceptional flow plz
        db = couch[accessdb]
            
        with open('{}.key'.format(accessdb),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
            key = file.read()
                    
        # #     username_byte = str.encode(username)
        # #     newhmac = hmac.new(key, username_byte, digestmod=hashlib.sha256)
        # #     MDauthen = newhmac.hexdigest()
        
        # #     if checkcre == MDauthen:
        # #             foundcheck = browsedoc33
        # # if foundcheck == "none":
        # #     print('Authentication Failed')
        # #     exit()
        foundcheck = findDoc.findDoc(key,username,accessdb)
        foundcheck = symcrytjson.decryptjson(key,foundcheck)

        print(foundcheck) # username, password, role
        role = foundcheck['role']
            
        if(role == "registrar"):            
            
            with open('{}.key'.format(accessdb),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                key = file.read()
        
            registrar.registrar(key,accessdb)
            
        elif(role == "medical staff"):
            
            view.views(key,accessdb)
            
        elif(role == "admin"):
            # action = input('Do you want to create or drop table? (create/drop) : ')
            
            # if(action == "create"):
            #     create()
            # elif(action == "drop"):
            #     drop()
            admin.admin(key)
    
index()