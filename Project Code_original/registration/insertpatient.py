
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import os
import symcrytjson
import registrar
def insertpatient(key,patientdb):
    try:
        # connect to the DB
        couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
        
        db = couch[patientdb] # main
        
        db_views = couch[patientdb+'_views']    # views
        
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")

    while(True):
        name = input("Enter name: ")
        if name == "exit":
            exit()
        elif name == "back":
            registrar.registrar(key,patientdb)
        while(True):
            NationalID = input("Enter National ID: ")
            if NationalID == "exit":
                exit()
            elif NationalID == "back":
                break
            while(True):
                address = input("Addres of residence: ")
                if address == "exit":
                    exit()
                elif address == "back":
                    break
                while(True):
                    Phonenum = input("Enter phone number: ")
                    if Phonenum == "exit":
                        exit()
                    elif Phonenum == "back":
                        break
                    while(True):
                        email = input("Email: ")
                        if email == "exit":
                            exit()
                        elif email == "back":
                            break
                        while(True):
                            fam_name = input("Name of family member: ")
                            if fam_name == "exit":
                                exit()
                            elif fam_name == "back":
                                break
                            while(True):
                                fam_contact = input("Contact of family member: ")
                                if fam_contact == "exit":
                                    exit()
                                elif fam_contact == "back":
                                    break
                                while(True):
                                    dob = input("Date of birth: ")
                                    if dob == "exit":
                                        exit()
                                    elif dob == "back":
                                        break
                                    while(True):
                                        nationality = input("Nationality: ")
                                        if nationality == "exit":
                                            exit()
                                        elif nationality == "back":
                                            break
                                        while(True):
                                            height = input("Height: ")
                                            if height == "exit":
                                                exit()
                                            elif height == "back":
                                                break
                                            while(True):
                                                weight = input("Weight: ")
                                                if weight == "exit":
                                                    exit()
                                                elif weight == "back":
                                                    break
                                                while(True):
                                                    bloodtype = input("Bloodtype: ")
                                                    if bloodtype == "exit":
                                                        exit()
                                                    elif bloodtype == "back":
                                                        break
                                                    while(True):
                                                        insurance_prov = input("Insurance provider: ")
                                                        if insurance_prov == "exit":
                                                            exit()
                                                        elif insurance_prov == "back":
                                                            break
                                                        while(True):
                                                            insurance_ID = input("Insurance ID : ")
                                                            if insurance_ID == "exit":
                                                                exit()
                                                            elif insurance_ID == "back":
                                                                break
                                                            while(True):
                                                                doctor = input("Responsible physician : ")
                                                                if doctor == "exit":
                                                                    exit()
                                                                elif doctor == "back":
                                                                    break
                                                                while(True):
                                                                    health_relate = input("Health-related behavior : ")
                                                                    if health_relate == "exit":
                                                                        exit()
                                                                    elif health_relate == "back":
                                                                        break
                                                                    while(True):
                                                                        Past_med = input("Past medical records: ")
                                                                        if Past_med == "exit":
                                                                            exit()
                                                                        elif Past_med == "back":
                                                                            break
                                                                        while(True):
                                                                            fam_hist = input("Family history: ")
                                                                            if fam_hist == "exit":
                                                                                exit()
                                                                            elif fam_hist == "back":
                                                                                break
                                                                            while(True):
                                                                                allergies = input("Allergies: ")
                                                                                if allergies == "exit":
                                                                                    exit()
                                                                                elif allergies == "back":
                                                                                    break
                                                                                section_no = patientdb[16]
                                                                                if section_no == 1:
                                                                                    dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section1_patient'
                                                                                elif section_no == 2:
                                                                                    dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section2_patient'
                                                                                elif section_no == 3:
                                                                                    dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section3_patient'
                                                                                else:
                                                                                    print("Invalid section")
                                                                                
                                                                                patient_no =len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))]) + 1
                                                                                patient_id_first2digits = "0{}".format(section_no)
                                                                                patient_id_last4digits = str(patient_no)
                                                                                while(len(patient_id_last4digits) != 4):
                                                                                    patient_id_last4digits = "0" + patient_id_last4digits

                                                                                patient_id = "p" + patient_id_first2digits + patient_id_last4digits
                                                                                print(patient_id)
                                                                                
                                                                                doc = {"id":"{}".format(patient_id),
                                                                                    "name":"{}".format(name),
                                                                                    "National ID":"{}".format(NationalID),
                                                                                    "Addres of residence":"{}".format(address),
                                                                                    "Phonenum":"{}".format(Phonenum),
                                                                                    "Email":"{}".format(email),
                                                                                    "Name of family member":"{}".format(fam_name),
                                                                                    "Contact of family member":"{}".format(fam_contact),
                                                                                    "dob":"{}".format(dob),
                                                                                    "nationality":"{}".format(nationality),
                                                                                    "height": "{}".format(height),
                                                                                    "weight":"{}".format(weight),
                                                                                    "bloodtype":"{}".format(bloodtype),
                                                                                    "Insurance Provider":"{}".format(insurance_prov),
                                                                                    "Insurance ID":"{}".format(insurance_ID),
                                                                                    "Responsible Physician":"{}".format(doctor),
                                                                                    "Health-related behavior : ":"{}".format(health_relate),
                                                                                    "Past medical records: ":"{}".format(Past_med),
                                                                                    "Family history: ":"{}".format(fam_hist),
                                                                                    "Allergies: ":"{}".format(allergies)}
                                                        
                                                        
                                                                                doc_views = {"id":"{}".format(patient_id),
                                                                                    "name":"{}".format(name),
                                                                                    "Phonenum":"{}".format(Phonenum),
                                                                                    "Name of family member":"{}".format(fam_name),
                                                                                    "Contact of family member":"{}".format(fam_contact),
                                                                                    "dob":"{}".format(dob),
                                                                                    "nationality":"{}".format(nationality),
                                                                                    "height": "{}".format(height),
                                                                                    "weight":"{}".format(weight),
                                                                                    "bloodtype":"{}".format(bloodtype),
                                                                                    "Insurance Provider":"{}".format(insurance_prov),
                                                                                    "Insurance ID":"{}".format(insurance_ID),
                                                                                    "Responsible Physician":"{}".format(doctor),
                                                                                    "Health-related behavior : ":"{}".format(health_relate),
                                                                                    "Past medical records: ":"{}".format(Past_med),
                                                                                    "Family history: ":"{}".format(fam_hist),
                                                                                    "Allergies: ":"{}".format(allergies)}
                                                                                
                                                                                #covert JSON to string
                                                                                doc_string = json.dumps(doc)
                                                                                doc_sorted = json.dumps(doc, indent = 3)
                                                                                print("Document: \n", doc_sorted)
                                                                                
                                                                                # docs for views
                                                                                doc_string_views = json.dumps(doc_views)
                                                                                doc_sorted_views = json.dumps(doc_views, indent = 3)
                                                                                print("Document: \n", doc_sorted_views)

                                                                                #encrypt the document
                                                                                doc_encrypted = symcrytjson.encryptjson(key,doc_string) 
                                                                                doc_encrypted_sorted = json.dumps(doc_encrypted, indent = 3)
                                                                                
                                                                                
                                                                                # docs for views
                                                                                doc_encrypted_views = symcrytjson.encryptjson(key,doc_string_views) 
                                                                                doc_encrypted_sorted_views = json.dumps(doc_encrypted_views, indent = 3)
                                                                                
                                                                                print("Encrypted view document: \n", doc_encrypted_sorted_views)
                                                                                print("Encrypted document: \n", doc_encrypted_sorted)
                                                                                
                                                                                while(True):
                                                                                    confirm = input("Do you want to insert the above encrypted document? (y/n/exit): ")
                                                                                    if confirm == "y":
                                                                                        try:
                                                                                            # main database
                                                                                            db.save(doc_encrypted)
                                                                                            
                                                                                            # views database
                                                                                            db_views.save(doc_encrypted_views)

                                                                                            #save to local storage
                                                                                            with open('./section{}_patient/{}_{}.json'.format(section_no,patient_id,name),'w') as file:
                                                                                                file.write(doc_sorted)
                                                                                            
                                                                                            print("The document has been saved to {}".format(db.name))
                                                                                            print("The document has been saved to {}".format(db_views.name))
                                                                                            
                                                                                        except(couchdb.http.ServerError):
                                                                                            print("Cannot save the document")
                                                                                        insertpatient(key,patientdb) #go back to the top
                                                                                    elif confirm == "n":
                                                                                        insertpatient(key,patientdb) #go back to the top
                                                                                    elif confirm == "exit":
                                                                                        exit()
                                                                                    else:
                                                                                        print("Invalid command, please try again")