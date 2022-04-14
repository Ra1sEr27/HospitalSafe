
"""Randomised One-Time Pad encryption and decryption functions in Python."""

import random

charset = " ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789" 
 

def main(vector):
    """Demo usage of functions."""
    encrypted = encrypt(vector) # return otp = en[0], result = en[1]
    decrypted = decrypt(encrypted[0], encrypted[1])

    print("Test Vector: " + vector)
    print("OTP: " + encrypted[0])
    print("Encrypted: " + encrypted[1])
    print("Decrypted: " + decrypted)
    

def encrypt(plaintext):
    """Encrypt plaintext value.
    Keyword arguments:
    plaintext -- the plaintext value to encrypt.
    """
    otp = "".join(random.sample(charset, len(charset)))
    result = ""

    for c in plaintext:
        if c not in otp:
            continue
        else:
            result += otp[charset.find(c)]

    return otp, result


def decrypt(otp, secret): #Secert = Plaintext
    """Decrypt secret value.
    Keyword arguments:
    otp -- the one-time pad used when the secret value was encrypted.
    secret -- the value to be decrypted.
    """
    result = ""

    for c in secret:
        if c not in otp:
            continue
        else:
            result += charset[otp.find(c)]

    return result


if __name__ == "__main__":
    main()