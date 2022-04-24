from cryptography.fernet import Fernet
from pymongo import MongoClient
import pymongo

client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
mydb = client['Hospital']

for dbname in mydb:
    print(dbname)