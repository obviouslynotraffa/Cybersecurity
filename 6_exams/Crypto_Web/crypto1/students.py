import base64
import string
import binascii

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)

with open('encrypted_flag.txt', 'r') as f:
    encrypted_message=f.read()

