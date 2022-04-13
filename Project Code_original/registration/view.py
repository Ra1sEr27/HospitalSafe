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
import getalldoc


def views(key, accessdb):
    while(True):
        username = 'nontawat'
        password = 'non123'
        try:
            # connect to the DB
            couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
                
            #db = couch['rbac']        
                
            #print("Access granted")
            break
        
        except(couchdb.http.Unauthorized):
            print("Invalid username or password")
            

        
    while(True):
        type = input("views all or search by patient's name ? (all/search/back/exit) : ")
        
        if type == 'exit':
            exit()
        elif type == "back":
            break
        
        elif type == "all":
            
            if(accessdb == "section1_staff"):
                viewsdb = "hospital_section1_views"
                
            elif(accessdb == "section2_staff"):
                viewsdb = "hospital_section2_views"
            
            elif(accessdb == "section3_staff"):
                viewsdb = "hospital_section3_views"
            
            elif(accessdb == "section4_staff"):
                viewsdb = "hospital_section4_views"
            
            elif(accessdb == "section5_staff"):
                viewsdb = "hospital_section5_views"
            else:
                print("Invalid database")
            
            getalldoc.getalldoc(key, viewsdb)
        
        
        elif type == "search":
            patientname = input("Enter patient name : ")
        
        
            if(patientname == "back"):
                break
            elif(patientname == "exit"):
                exit()
            else:
                if(accessdb == "section1_staff"):
                    viewsdb = "hospital_section1_views"
                
                elif(accessdb == "section2_staff"):
                    viewsdb = "hospital_section2_views"
                
                elif(accessdb == "section3_staff"):
                    viewsdb = "hospital_section3_views"
                
                elif(accessdb == "section4_staff"):
                    viewsdb = "hospital_section4_views"
                
                elif(accessdb == "section5_staff"):
                    viewsdb = "hospital_section5_views"
                else:
                    print("Invalid database")
                
                foundcheck = 'none'
                
                foundcheck = findDoc.findDoc(key,patientname,viewsdb)
                
                if(foundcheck == 'none'):
                    print('Patient not found')
                
                else:
                    foundcheck = symcrytjson.decryptjson(key,foundcheck)
                    foundcheck_sorted = json.dumps(foundcheck, indent = 6)
                    print("{}'s document: \n{}".format(patientname,foundcheck_sorted))
                
        
    