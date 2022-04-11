from Crypto.Cipher import AES
from secrets import token_bytes
import couchdb
import json

couch = couchdb.Server('http://nontawat:debsirin45063@localhost:5984/')
db = couch['thammasat_hospital']
key = token_bytes(32)

def encrypt(msg):
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    return nonce, ciphertext, tag

def decrypt(nonce, ciphertext, tag):
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(ciphertext)
    try:
        cipher.verify(tag)
        return plaintext.decode('ascii')
    except:
        return False

nonce, ciphertext, tag = encrypt(input('Enter a message: '))
plaintext = decrypt(nonce, ciphertext, tag)
print(f'Cipher text: {ciphertext}')
print(f'Key: {key}')
print(f'Nonce: {nonce}')
print(f'Tag: {tag}')
nonjsondoc = {ciphertext}
doc = json.dumps(nonjsondoc)
print(nonjsondoc)
db.save(doc)
doc

if not plaintext:
    print('Message is corrupted')
else:
    print(f'Plain text: {plaintext}')

