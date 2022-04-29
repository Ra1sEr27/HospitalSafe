from types import NoneType
from cryptography.fernet import Fernet
import hmac, hashlib
import getpass
import findDoc
import symcrytjson
import getpass
import view
import admin
import registrar
import symcrytjson
import timeit
def index():
    while(True):
        id = input("please insert id : ")
        if id == "exit":
            exit()
        password = getpass.getpass("please insert password : ")
        if password == "exit":
            exit()
        if password != "": #password is not blank
            start = timeit.default_timer()
        
        
        ############## finding admin ##############
        
        with open('admin.key', 'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
            admin_key = file.read()
        
        

        wanteddoc = findDoc.findDoc(admin_key,id,"admin") #find document in admin database
        if type(wanteddoc) != NoneType: #user is admin
            #print(wanteddoc)
            start = timeit.default_timer()
            decryptcheck = symcrytjson.decryptjson(admin_key, wanteddoc)
            stop = timeit.default_timer()
            print('Time: ', stop - start)
            id_check = decryptcheck["id"]
            #hash the password
            password_byte = str.encode(password)
            hmac1 = hmac.new(admin_key, password_byte, digestmod=hashlib.sha256)
            #Create password MD from hmac1
            hashedpassword = hmac1.hexdigest() #hashed password from input
            print(hashedpassword)
            password_check = decryptcheck["password"] #stored password
            sa = 'a' # admin
        
        ############## finding a staff ##############
        section_no=0
        while type(wanteddoc) == NoneType: #find staff's document in every staff database when the user is not an admin
            section_no += 1
            #print(section_no)
            if section_no==4:
                print("There is no {}'s document stored in the system".format(id))
                sa = "none" # not found any staff / admin
                
                # worst case runtime 
                stop = timeit.default_timer()
                print('Time: ', stop - start)
                
                break
            with open('section{}-staff.key'.format(section_no),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                key_selected = file.read()

            wanteddoc = findDoc.findDoc(key_selected,id,"section{}-staff".format(section_no))
            sa = 's' # staff
            
        if(sa == 's'): #if user is staff
            print("test")
            decryptcheck = symcrytjson.decryptjson(key_selected, wanteddoc)
            #print(decryptcheck)
            if not decryptcheck: #if cannot decrypt the document
                print("Please re-login. Sorry for inconvenient")
                index()
            id_check = decryptcheck["id"]
            #hash the password
            password_byte = str.encode(password)
            hmac1 = hmac.new(key_selected, password_byte, digestmod=hashlib.sha256)
            #Create password MD from hmac1
            hashedpassword = hmac1.hexdigest() #hashed password from input
            print(hashedpassword)
            password_check = decryptcheck["password"]
            
            #print(id_check+" "+password_check)
            #print(id+" "+password)

        if(sa != "none" and id == id_check and hashedpassword == password_check): # authenticated
            print("test1")
            if(sa == 's'):
                decdoc = symcrytjson.decryptjson(key_selected,wanteddoc)
                known_sec = decdoc['accessdb'] # accessdb            
            
            #print(decryptcheck) # id, password, role
            role = decryptcheck['role']
            
            if(role == "admin"):
                #with open('admin.key','rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                #    admin_key = file.read()
                print("---Welcome to admin section---")
                admin.admin(admin_key,id)
                
            if(role == "registrar"):            
                print("---Welcome to registrar section---")
                with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    staff_key = file.read()
                    
                registrar.registrar(staff_key,known_sec)
                
            elif(role == "medical staff"):
                print("---Welcome medical staff section---")
                with open('{}.key'.format(known_sec),'rb') as file:  #section1_staff.key , section2_staff.key, section3_staff.key . . . , section5_staff.key
                    staff_key = file.read()
                view.views(staff_key,known_sec)

        elif hashedpassword != password_check: #The inputted passsword is not matched with the stored password
            print("Incorrect password. Please try again.")
index()