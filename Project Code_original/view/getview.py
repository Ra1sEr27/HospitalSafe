#this imports the cryptography package
from cryptography.fernet import Fernet
import getpass
import couchdb
import hashlib, hmac
#binasc
import sys
from cloudant import couchdb_admin_party
from cloudant.result import Result

db_name = 'hostpital_section1'
ddoc_id = 'd3193c34a42238ddbd7cb790b80322a2'
view_id = '_design/onlyCT'

with couchdb_admin_party(url='http://localhost:5984') as client:
    db = client.get(db_name, remote=True)
    view = db.get_design_document(ddoc_id).get_view(view_id)

    with open('/tmp/results.txt', 'w') as f:
        for result in Result(view, page_size=1000):
            f.write(result.get('key') + '\n')