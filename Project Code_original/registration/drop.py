from cryptography.fernet import Fernet
from pymongo import MongoClient
import pymongo

def drop():
    #code for testing

    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1-patient?retryWrites=true&w=majority")
    mydb = client['Hospital']
    while(True): #keep asking for db name
        colname = input("Enter collection name: ")
        #type "exit" to terminate the program
        if colname == "exit":
            exit()
        elif colname == "back":
            break
            
        else:
            while(True): #keep asking for comfirmation
                confirm = input("Do you want to delete the {} database? (y/n/exit): ".format(colname))
                if confirm == "y":
                    mycol = mydb[colname]
                    
                    mycol.drop()
                    print("Database {} has been deleted".format(colname))
                    break
                elif confirm == "n":
                    break
                elif confirm == "exit":
                    exit()
                else:
                    print("Invalid input, please try again")
