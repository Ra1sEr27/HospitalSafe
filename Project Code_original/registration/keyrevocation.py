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
            db = couch["section{}_staff".format(target_section)]
            break
        else:
            print("Invalid section, please try again")

    db.cleanup()