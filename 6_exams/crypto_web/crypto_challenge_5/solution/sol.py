
import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

def base32decode(message):
    return base64.b32decode(message).decode('ascii')


def XORdecode(message, KEY="Hug0"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

with open('../encrypted_flag', 'rb') as f:
    encrypted_flag = f.read().decode('ascii')
    f.close()
    
decoded = XORdecode(encrypted_flag)
decoded = base32decode(decoded)
print(decoded)