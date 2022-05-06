from cryptography.fernet import Fernet
from pymongo import MongoClient
import pymongo
import os, shutil
def drop():
    #code for testing

    client = pymongo.MongoClient("mongodb+srv://Nontawat:non@section1.oexkw.mongodb.net/section1?retryWrites=true&w=majority")
    mydb = client['Hospital']
    while(True):
        staffcolnumlist = []
        allcollist = mydb.list_collection_names()
        for i in range(len(allcollist)):
            if "staff" in allcollist[i]:
                staffcolnumlist.append(allcollist[i][7])
        sorted_staffcolnumlist = []
        for i in range(len(staffcolnumlist)):
            sorted_staffcolnumlist.append(int(staffcolnumlist[i]))
        sorted_staffcolnumlist.sort()
        colnum = input("Enter collection number (Existed collection number {}): ".format(sorted_staffcolnumlist))
        if colnum == "exit":
            exit()
        elif colnum == "back":
            break
        elif colnum in staffcolnumlist:
            colname = "section{}".format(colnum)
            patientcol = "section{}-patient".format(colnum)
            staffcol = "section{}-staff".format(colnum)
            while(True): #keep asking for comfirmation
                confirm = input("Do you want to delete {} collection? (y/n/exit): ".format(colname))
                if confirm == "y":
                    mycol = mydb[patientcol]
                    mycol.drop() #drop collection in MongoDB
                    foldername = patientcol
                    directory = os.path.abspath('.')
                    patientfolder_dir = os.path.join(directory, foldername)
                    print(patientfolder_dir)
                    for filename in os.listdir(patientfolder_dir): #empty the patient's folder
                        file_path = os.path.join(patientfolder_dir, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        except Exception as e:
                            print('Failed to delete %s. Reason: %s' % (file_path, e))
                    path_dir = "C:/Users/exia4/OneDrive/Desktop/SIIT/Third Year/Second Semester/Network Security/Project/Security-and-Cloud-Project/Project Code_original/Code/"
                    if os.path.exists(directory): #remove folder
                        os.rmdir(os.path.join(path_dir, directory))
                    mycol = mydb[staffcol]
                    mycol.drop()
                    foldername = staffcol
                    directory = os.path.abspath('.')
                    stafffolder_dir = os.path.join(directory, foldername)
                    for filename in os.listdir(stafffolder_dir): #empty the staff's folder
                        file_path = os.path.join(stafffolder_dir, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                        except Exception as e:
                            print('Failed to delete %s. Reason: %s' % (file_path, e))
                    path_dir = "C:/Users/exia4/OneDrive/Desktop/SIIT/Third Year/Second Semester/Network Security/Project/Security-and-Cloud-Project/Project Code_original/Code/"
                    if os.path.exists(directory):
                        os.rmdir(os.path.join(path_dir, directory))
                    print("Collection {} has been deleted".format(colname))
                    f = open('section{}-staff.key'.format(colnum), 'w') #delete local file
                    f.close()
                    os.remove(f.name)
                    break
                elif confirm == "n":
                    break
                elif confirm == "exit":
                    exit()
                else:
                    print("Invalid input, please try again")
        else:
            print("Invalid collection number")