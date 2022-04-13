from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii
import insertpatient
import updatepatient
import deletepatient
import insertadmin_registrar_staff
import deletestaff
import updatestaff
import registrar

with open('section1_staff.key', 'rb') as file:
    key = file.read()
registrar.registrar(key,"db1")