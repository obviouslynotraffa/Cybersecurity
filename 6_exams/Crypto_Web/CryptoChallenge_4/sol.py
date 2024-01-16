import base64
import string
import binascii

ALPHABET = list(string.printable)  
LEN = len(ALPHABET)


def ROTdecode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - pos)%LEN]
    return rot13_enc

def base64decode(cipher):
    return base64.b64decode(cipher).decode('ascii', errors="ignore")

with open('encrypted_flag.txt', 'r') as f:
    encrypted_message=f.read()
    f.close()

decoded = ROTdecode(encrypted_message, 13)
decoded = base64decode(decoded)

print(decoded)
