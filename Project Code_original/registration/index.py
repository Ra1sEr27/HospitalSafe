from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import create 
import drop
import findDoc
import symcrytjson
import getpass
import view
import admin
import registrar
import symcrytjson
import timeit
def index():
    try:
        # connect to the DB
        couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")

    while(True):
        authentication = False
        while(True):
            username = input("please insert name : ")
            password = getpass.getpass("please insert password : ")
            
            if(password != ''):
                start = timeit.default_timer()
            
            ############## finding admin ##############
            
            with open('admin.key', 'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                admin_key = file.read()
            
            wanteddoc = findDoc.findDoc(admin_key,username,"admin") #find document in admin database
            if wanteddoc != "none":
                decryptcheck = symcrytjson.decryptjson(admin_key, wanteddoc)
                #print(decryptcheck)
                username_check = decryptcheck["name"]
                password_check = decryptcheck["password"]
                sa = 'a' # admin
            
            ############## finding a staff ##############
            
            section_no=0
            while wanteddoc == "none": #find registrar's document in every staff database when the user is not an admin
                section_no += 1
                if section_no==3:
                    print("There is no {}'s document stored in the system".format(username))
                    sa = "none" # not found any staff / admin
                    
                    # worst case runtime 
                    stop = timeit.default_timer()
                    print('Time: ', stop - start)
                     
                    break
                with open('section{}_staff.key'.format(section_no),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    key_selected = file.read()
                    
                wanteddoc = findDoc.findDoc(key_selected,username,"section{}_staff".format(section_no))
                sa = 's' # staff
                

            if(sa == 's'):
                
                decryptcheck = symcrytjson.decryptjson(key_selected, wanteddoc)
                username_check = decryptcheck["name"]
                password_check = decryptcheck["password"]
                
                
            #print(username_check+" "+password_check)
            #print(username+" "+password)
            
            if(sa != "none" and username == username_check and password == password_check): # authenticated
                
                if(sa == 's'):
                    decdoc = symcrytjson.decryptjson(key_selected,wanteddoc)
                    known_sec = decdoc['accessdb'] # accessdb            
                
                #print(decryptcheck) # username, password, role
                role = decryptcheck['role']
                
                if(role == "admin"):
                    #with open('admin.key','rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    #    admin_key = file.read()
                    print("---Welcome to admin section---")
                    admin.admin(admin_key,username)
                    
                if(role == "registrar"):            
                    print("---Enter registrar section---")
                    with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                        staff_key = file.read()
                        
                    registrar.registrar(staff_key,known_sec)
                    
                elif(role == "medical staff"):
                    print("---Enter medical staff section---")
                    with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                        staff_key = file.read()
                        
                    view.views(staff_key,known_sec)
    
index()