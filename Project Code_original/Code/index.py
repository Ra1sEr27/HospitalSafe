from cryptography.fernet import Fernet
import hmac, hashlib
import getpass
import findDoc
import symcrytjson
import admin
import registrar
import symcrytjson
import getview
import pymongo,checkKVL, updatepassword


NoneType = type(None)
def index():
    while(True):
        id = input("please insert id : ")
        if id == "exit":
            exit()
        password = getpass.getpass("please insert password : ")
        if password == "exit":
            exit()
            
        with open('admin.key', 'rb') as file: #open admin's key
            admin_key = file.read()
        wanteddoc = findDoc.findDoc(admin_key,id,"admin") #find document in admin database
        if type(wanteddoc) != NoneType: #user is admin
            decryptcheck = symcrytjson.decryptjson(admin_key, wanteddoc)
            id_check = decryptcheck["id"]
            #hash the password
            password_byte = str.encode(password)
            hmac1 = hmac.new(admin_key, password_byte, digestmod=hashlib.sha256)
            #Create password MD from hmac1
            hashedpassword = hmac1.hexdigest() #hashed password from input
            #print(hashedpassword)
            password_check = decryptcheck["password"] #stored password
            sa = 'a' # admin
            if hashedpassword != password_check: #The inputted passsword is not matched with the stored password
                revokestatus, key = checkKVL.checkKVL(id) #check revoke status
                if revokestatus: #try to hash with the old key(if any)
                    admin_key = str.encode(key) 
                    hmac1 = hmac.new(admin_key, password_byte, digestmod=hashlib.sha256)
                    #Create password MD from hmac1
                    hashedpassword = hmac1.hexdigest() #hashed password from input
                    if hashedpassword != password_check:
                        print("Incorrect password. Please try again.")
                    
                elif not revokestatus:
                    print("Incorrect password. Please try again.")
        
        #find staff's document
        section_no=0
        client = pymongo.MongoClient("mongodb+srv://Nontawat:iS1sKbQnyLO6CWDE@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
        mydb = client["Hospital"]
        staffcolnumlist = []
        allcollist = mydb.list_collection_names()
        for i in range(len(allcollist)):
            if "staff" in allcollist[i]:
                staffcolnumlist.append(allcollist[i][7])
        sorted_staffcolnumlist = []
        for i in range(len(staffcolnumlist)):
            sorted_staffcolnumlist.append(int(staffcolnumlist[i]))
        sorted_staffcolnumlist.sort()
        
        while type(wanteddoc) == NoneType: #find staff's document in every staff database when the user is not an admin
            section_no += 1
            if section_no == len(staffcolnumlist):
                print("There is no {}'s document stored in the system".format(id))
                sa = "none" # not found any staff / admin
                break
            with open('section{}-staff.key'.format(section_no),'rb') as file:
                key_selected = file.read()
            
            wanteddoc = findDoc.findDoc(key_selected,id,"section{}-staff".format(section_no))
            sa = 's' # staff
            
        if(sa == 's'): #if user is staff
            decryptcheck = symcrytjson.decryptjson(key_selected, wanteddoc)
            if not decryptcheck: #if cannot decrypt the document
                print("Please re-login. Sorry for inconvenient")
                index()
            id_check = decryptcheck["id"]
            
            #hash the password
            password_byte = str.encode(password)
            hmac1 = hmac.new(key_selected, password_byte, digestmod=hashlib.sha256)
            #Create password MD from hmac1
            hashedpassword = hmac1.hexdigest() #hashed password from input
            #print(hashedpassword)
            password_check = decryptcheck["password"]
            if hashedpassword != password_check: #The inputted passsword is not matched with the stored password
                revokestatus, key = checkKVL.checkKVL(id) #check revoke status
                if revokestatus: #use old key to hash the password
                    key_selected = str.encode(key)
                    hmac1 = hmac.new(key_selected, password_byte, digestmod=hashlib.sha256)
                    #Create password MD from hmac1
                    hashedpassword = hmac1.hexdigest() #hashed password from input
                    if hashedpassword != password_check:
                        print("Incorrect password. Please try again.")
                elif not revokestatus: #never get revoked
                    print("Incorrect password. Please try again.")
                

        if(sa != "none" and id == id_check and hashedpassword == password_check): # authenticated
            if(sa == 's'): #user is staff
                with open('section{}-staff.key'.format(section_no),'rb') as file: 
                    key_selected = file.read()
                decdoc = symcrytjson.decryptjson(key_selected,wanteddoc)
                known_sec = decdoc['accessdb'] # accessdb
            if(sa == 'a'): #user is admin
                with open('admin.key','rb') as file: 
                    key_selected = file.read()
                decdoc = symcrytjson.decryptjson(key_selected,wanteddoc)
                known_sec = decdoc['accessdb'] # accessdb
            revokestatus, key = checkKVL.checkKVL(id)
            if revokestatus: #update the password
                hmac1 = hmac.new(key_selected, password_byte, digestmod=hashlib.sha256)
                #Create password MD from hmac1
                hashedpassword = hmac1.hexdigest() #hashed password
                updatepassword.updatepassword(wanteddoc,decdoc,hashedpassword,key_selected)
                
            role = decryptcheck['role']
            if(role == "admin"):
                print("---Welcome to admin section---")
                admin.admin(admin_key,id)
                
            if(role == "registrar"):            
                print("---Welcome to registrar section---")
                with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    staff_key = file.read()
                if int(known_sec[7]) in sorted_staffcolnumlist: 
                    registrar.registrar(staff_key,known_sec[7])
                
            elif(role == "medical staff"):
                print("---Welcome to medical staff section---")
                with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    staff_key = file.read()
                getview.getview(known_sec[7])

index()