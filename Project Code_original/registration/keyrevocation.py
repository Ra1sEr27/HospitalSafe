import keygenerator
import couchdb

def keyrevocation(target_section):
    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')
    while(True):
        #target_section = input("Enter the compromised section (0-3) : ")
        if target_section == "0":   #target section = admin section
            keygenerator.re_adminkeygenerator()
            db = couch["admin"]
            break
        elif target_section in ("1","2","3"):
            keygenerator.re_staffkeygenerator(target_section)
            staffdb = couch["section{}_staff".format(target_section)]
            patientdb = couch["hospital_section{}".format(target_section)]
            break
        else:
            print("Invalid section, please try again")
            break
    for docid in staffdb.view('_all_docs'): #delete all documents in compromised staff section
        i = docid['id']
        browsedoc = staffdb[i]
        staffdb.delete(browsedoc)

    for docid in patientdb.view('_all_docs'): #delete all documents in compromised patient section
        i = docid['id']
        browsedoc = patientdb[i]
        patientdb.delete(browsedoc)

    with open('section{}_staff.key'.format(target_section),'rb') as file:
            new_key = file.read()