from cryptography.fernet import Fernet

def keygenerator(section_no): #For generating the key for a new section
    #section_no = input("Enter the section number : ")
    key = Fernet.generate_key()
    with open('section{}-staff.key'.format(section_no),'wb') as file:
        file.write(key)

def re_staffkeygenerator(target_section): #For regenerating the existed section key
    key = Fernet.generate_key()
    with open('section{}-staff.key'.format(target_section),'wb') as file:
        file.write(key)

def re_adminkeygenerator(): #For regenerating the admin section key
    key = Fernet.generate_key()
    with open('admin.key','wb') as file:
        file.write(key)
#keygenerator()