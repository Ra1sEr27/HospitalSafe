from cryptography.fernet import Fernet

filename = input("Enter the key's file name : ")
key = Fernet.generate_key()
with open('{}.key'.format(filename),'wb') as file:
    file.write(key)