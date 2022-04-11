import couchdb
import json
import hashlib, hmac

class checkauthen():
    
    def authen(self):
        
        username = 'nontawat'
        password = 'non123'

        couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))

        username = input("please insert username : ")
        password = input("please insert password : ")

        rbac = couch['rbac']

        foundcheck = "none"
        for docid in rbac.view('_all_docs'):
            i = docid['id']
            browsedoc33 = rbac[i]
                
            checkcre = browsedoc33['MD']
            
            newhmac = hmac.new(username, password, digestmod=hashlib.sha256)
            MDauthen = newhmac.hexdigest()
    
            if checkcre == MDauthen:
                    foundcheck = browsedoc33
        if foundcheck == "none":
            print('Authentication Failed')
            exit()       
            authen = False       
        else:
            print(foundcheck) # username, password, role
            authen = True
                
        role = foundcheck['role'] # user role
        accessdb = foundcheck['db'] # user access which database
        return role
        return accessdb
        return authen