# HospitalSafe
  An application for allowing a hospital staff to manage the patient's document safely, to able to access anywhere in the private network. 
  With a security and cloud features provided.
  - Features
    - RBAC (Role-based Access Control) for control the access of users (Admin, Registrar, and Medical Staff)
    - AES (Advanced Encryption System) for patient document encryption.
    - SHA-256 (Hashing Algorithm) for message digest generation (use for indexing the encrypted patient documents on cloud)
    - HMAC (Hash-based Message Authentication Code) for integrity checking of patient document.
    - Use of MongoDB as a cloud storage for storing encrypted patient documents.
  - System Diagram
    - Encryption
    
      ![image](https://user-images.githubusercontent.com/94690219/174238196-d6b9b76c-659b-4a87-8920-ff6cf6825d95.png)
    - Decryption
    
      ![image](https://user-images.githubusercontent.com/94690219/174238284-2d0aa6d5-83a4-4807-9291-b3f27a5d491a.png)
    - Key Revocation
    
      ![image](https://user-images.githubusercontent.com/94690219/174238511-bc962edc-0d46-4515-94f2-ba5fd24806e0.png)
    - Ciphertext Regeneration
    
      ![image](https://user-images.githubusercontent.com/94690219/174238582-eb7ac28c-a980-476c-9c4e-a614a4598bda.png)

  - Data Structure of patient document (On-Premise & On-Cloud)
    - Plaintext (On-Premise)
    
       ![image](https://user-images.githubusercontent.com/94690219/173511853-7f2c5aa0-54c3-486e-93a7-4ea6f5797d76.png)
    - Ciphertext (On-Cloud)
    
       ![image](https://user-images.githubusercontent.com/94690219/173513367-a3a85f8c-0b61-436c-a2c4-349c7c5a3f0d.png)
  
  For the IEEE report of our project, click [here](https://docs.google.com/document/d/1MAH50E3cNIuhP8d7eeDTgi6Miu0p6SpwnStbSjQDf6w/edit?usp=sharing).
  
Manual for setting up our program.
1) Open [MongoDB](https://account.mongodb.com/account/login?n=%2Fv2%2F62655d42f88180009011aa95%23security%2Fnetwork%2FaccessList) and login with this email and password.
    Email: 6222770735@g.siit.tu.ac.th
    Password: OOzyISp1Fh9lIbOp
2) Get your IP address by clicking [here](https://www.whatismyip.com/).
3) Go to cluster name "section1" and click on "Netwok Access" at the left tab.
4) Click at "Add IP Address" green button which located at the top right corner of the page.
5) Enter the IP Address from step 3 and your address name.
6) Click "Confirm" button.
7) Type the following commands in your terminal to install the required librarys
    - pip install cryptography
    - pip install hmac
    - pip install hashlib
    - pip install pymongo
8) Type in the following command in the terminal "python index.py".

Manual for logging in to the system.
1) Use ID of the user (Can be known by looking at the local file name) as ID.
2) Use firstname(lowercase) of the user and follow with "123" as a password.
