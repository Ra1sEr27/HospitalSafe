from cryptography.fernet import Fernet
import onetimepad
import getpass
import couchdb
import json
import hashlib
import hmac
import binascii


# def update(key,username,password):
#     couch = couchdb.Server('http://{}:{}@localhost:5984/'.format(username,password))
    # while(True): #keep the program running
    #     while(True): #keep asking for db name
    #         dbname = input("Enter database name: ")
    #         #type "exit" to terminate the program
    #         if dbname == "exit":
    #             exit()
    #         elif dbname not in couch:
    #             print("Database {} is not existed, please re-enter the database name.".format(dbname))
    #         else:
    #             break
    #     while(True): #keep asking for comfirmation
    #         confirm = input("Do you want to delete the {} database? (y/n/exit): ".format(dbname))
    #         if confirm == "y":
    #             couch.delete(dbname)
    #             print("Database {} has been deleted".format(dbname))
    #             break
    #         elif confirm == "n":
    #             break
    #         elif confirm == "exit":
    #             exit()
    #         else:
    #             print("Invalid input, please try again")
def drop():
    #code for testing

    couch = couchdb.Server('http://nontawat:non123@localhost:5984/')


    while(True): #keep asking for db name
        dbname = input("Enter database name: ")
        #type "exit" to terminate the program
        if dbname == "exit":
            exit()
        elif dbname == "back":
            break
        elif dbname not in couch:
            print("Database {} is not existed, please re-enter the database name.".format(dbname))
        else:
            while(True): #keep asking for comfirmation
                confirm = input("Do you want to delete the {} database? (y/n/exit): ".format(dbname))
                if confirm == "y":
                    couch.delete(dbname)
                    print("Database {} has been deleted".format(dbname))
                    break
                elif confirm == "n":
                    break
                elif confirm == "exit":
                    exit()
                else:
                    print("Invalid input, please try again")