
from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import os
import symcrytjson
import registrar
from pymongo import MongoClient
import pymongo
def insertpatient(key,patientdb):
    
    try:
        # connect to the DB
        client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
        mydb = client['Hospital']
        mycol = mydb[patientdb]
    except(couchdb.http.Unauthorized):
        print("Invalid username or password")
    if entername() == "back":
        registrar.registrar(key,patientdb)
    #print(patientdb)
    section_no = patientdb[16]
    #print(section_no)
    if section_no == "1":
        dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section1_patient'
    elif section_no == "2":
        dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section2_patient'
    elif section_no == "3":
        dir_path = r'C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project\Security-and-Cloud-Project\Project Code_original\registration\section3_patient'
    else:
        print("Invalid section")
    
    patient_id_first2digits = str(section_no)
    while(len(patient_id_first2digits) != 2):
        patient_id_first2digits = "0" + patient_id_first2digits
    
    patient_id_last4digits = 0
    patient_id = "p" +patient_id_first2digits + "000" + str(patient_id_last4digits)
    dir_list = os.listdir(dir_path)
    dir_list_onlyID = []
    for i in range(len(dir_list)): #append all of the file names from the chosen folder
        dir_list_onlyID.append(dir_list[i][:7])
    print(dir_list_onlyID)
    while(patient_id in dir_list_onlyID): #increase the number of last 4 digits
        patient_id_last4digits = int(patient_id_last4digits)
        patient_id_last4digits += 1
        patient_id_last4digits = str(patient_id_last4digits)
        
        while(len(patient_id_last4digits) != 4): #pad 0 to the left of last 4 digits
            patient_id_last4digits = "0" + patient_id_last4digits
            print("in loop ",patient_id_last4digits)
        patient_id = "p" +patient_id_first2digits + str(patient_id_last4digits)

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
        "Health-related behavior":"{}".format(health_relate),
        "Past medical records":"{}".format(Past_med),
        "Family history":"{}".format(fam_hist),
        "Allergies":"{}".format(allergies)}

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
        "Health-related behavior":"{}".format(health_relate),
        "Past medical records":"{}".format(Past_med),
        "Family history":"{}".format(fam_hist),
        "Allergies":"{}".format(allergies)}
    
    #covert JSON to string
    doc_string = json.dumps(doc)
    doc_sorted = json.dumps(doc, indent = 3)
    print("Document: \n", doc_sorted)
    
    # docs for views
    doc_string_views = json.dumps(doc_views)
    doc_sorted_views = json.dumps(doc_views, indent = 3)
    print("ViewDocument: \n", doc_sorted_views)

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
                id = mycol.insert_one(doc_encrypted)
                print("The document has been saved to {} (id: {}).".format(patientdb,id.inserted_id))
                #save to local storage
                with open('./section{}_patient/{}_{}.json'.format(section_no,patient_id,name),'w') as file:
                    file.write(doc_sorted)
                
                print("The document has been saved to {} (id: {}).".format(patientdb,id.inserted_id))
                
            except(couchdb.http.ServerError):
                print("Cannot save the document")
            insertpatient(key,patientdb) #go back to the top
        elif confirm == "n":
            insertpatient(key,patientdb) #go back to the top
        elif confirm == "exit":
            exit()
        else:
            print("Invalid command, please try again")

def entername():
    global name
    name = input("Enter name: ")
    if name == "exit":
        exit()
    elif name == "back":
        return "back"
    enterNationalID()
        
def enterNationalID():
    global NationalID
    NationalID = input("Enter National ID: ")
    if NationalID == "exit":
        exit()
    elif NationalID == "back":
        entername()
    enterAddress()

def enterAddress():
    global address
    address = input("Address of residence: ")
    if address == "exit":
        exit()
    elif address == "back":
        enterAddress()
    enterPhonenum()

def enterPhonenum():
    global Phonenum
    Phonenum = input("Enter phone number: ")
    if Phonenum == "exit":
        exit()
    elif Phonenum == "back":
        enterPhonenum()
    enterEmail()

def enterEmail():
    global email
    email = input("Email: ")
    if email == "exit":
        exit()
    elif email == "back":
        enterEmail()
    enterFamname()

def enterFamname():
    global fam_name
    fam_name = input("Name of family member: ")
    if fam_name == "exit":
        exit()
    elif fam_name == "back":
        enterEmail()
    enterFamnum()

def enterFamnum():
    global fam_contact
    fam_contact = input("Contact of family member: ")
    if fam_contact == "exit":
        exit()
    elif fam_contact == "back":
        enterFamname()
    enterdob()

def enterdob():
    global dob
    dob = input("Date of birth: ")
    if dob == "exit":
        exit()
    elif dob == "back":
        enterFamnum()
    enterNationality()

def enterNationality():
    global nationality
    nationality = input("Nationality: ")
    if nationality == "exit":
        exit()
    elif nationality == "back":
        enterdob()
    enterHeight()

def enterHeight():
    global height
    height = input("Height: ")
    if height == "exit":
        exit()
    elif height == "back":
        enterNationality()
    enterWeight()

def enterWeight():
    global weight
    weight = input("Weight: ")
    if weight == "exit":
        exit()
    elif weight == "back":
        enterHeight()
    enterBloodtype()

def enterBloodtype():
    global bloodtype
    bloodtype = input("Bloodtype: ")
    if bloodtype == "exit":
        exit()
    elif bloodtype == "back":
        enterWeight()
    enterInsprovider()

def enterInsprovider():
    global insurance_prov
    insurance_prov = input("Insurance provider: ")
    if insurance_prov == "exit":
        exit()
    elif insurance_prov == "back":
        enterBloodtype()
    enterInsID()

def enterInsID():
    global insurance_ID
    insurance_ID = input("Insurance ID : ")
    if insurance_ID == "exit":
        exit()
    elif insurance_ID == "back":
        enterInsprovider()
    enterdoctor()

def enterdoctor():
    global doctor
    doctor = input("Responsible physician : ")
    if doctor == "exit":
        exit()
    elif doctor == "back":
        enterInsID()
    enterHealth_related_behavior()

def enterHealth_related_behavior():
    global health_relate
    health_relate = input("Health-related behavior : ")
    if health_relate == "exit":
        exit()
    elif health_relate == "back":
        enterdoctor()
    enterPastMedRecord()
        
def enterPastMedRecord():
    global Past_med
    Past_med = input("Past medical records: ")
    if Past_med == "exit":
        exit()
    elif Past_med == "back":
        enterHealth_related_behavior()
    enterFamHistory()

def enterFamHistory():
    global fam_hist
    fam_hist = input("Family history: ")
    if fam_hist == "exit":
        exit()
    elif fam_hist == "back":
        enterPastMedRecord()
    enterAllergy()

def enterAllergy():
    global allergies
    allergies = input("Allergies: ")
    if allergies == "exit":
        exit()
    elif allergies == "back":
        enterFamHistory()
        
