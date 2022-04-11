import sys
import couchdb
import json
import sys
sys.path.append('C:\Users\exia4\OneDrive\Desktop\SIIT\Third Year\Second Semester\Network Security\Project')
import checkauthen

username = 'nontawat'
password = 'non123'

role1 = checkauthen()
role = role1.authen()

class checkpriv():

    def privlist():
    
        couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username, password))

        priv = couch['priviledge']

        foundcheck_priv = "none"
        for docid in priv.view('_all_docs'):
            i = docid['id']
            browsedoc33 = priv[i]

            checkcre1 = browsedoc33['role']  # looking for role attribute

            if checkcre1 == role:  # if found
                foundcheck_priv = browsedoc33  # it is this doc
        if foundcheck_priv == "none":
            print('Authenticate Failed')
            exit()
        else: # found
            # privilege = true false value
            priv_i = foundcheck_priv['insert'] 
            priv_r = foundcheck_priv['read']
            priv_u = foundcheck_priv['update']
            priv_d = foundcheck_priv['delete']
            print(foundcheck_priv)  # username, password, role
            return priv_i, priv_r, priv_u, priv_d

