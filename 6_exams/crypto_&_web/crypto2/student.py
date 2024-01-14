#!/usr/bin/env python3

import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

FLAG = "??????????????????????????????????????"

# base32 encoding
def base32encode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32encode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

# I think I'm forgetting something important to remove here
def XORencode(message, KEY="Hug0"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

# operations to reverse (you can comment these 2 lines)
encrypted = base32encode(FLAG)
encrypted = XORencode(message=encrypted)

# with open('encrypted_flag', 'wb') as f:
#     f.write(encrypted.encode('ascii'))
#     f.close()

# HELP RETRIEVE THE ENCRYPTED TEXT
with open('encrypted_flag', 'rb') as f:
    encrypted_flag = f.read().decode('ascii')

# DO YOUR STUFF