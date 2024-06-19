#!/usr/bin/env python3

import string
import itertools

XOR_KEY='??' # can be only letters

# read the file with the encrypted message
with open('encrypted', 'r') as f:
    encrypted_message=f.read()
    
def xor(txt, key):
    result = ''
    for c,k in zip(txt, itertools.cycle(key)):
        result += chr(ord(c) ^ ord(k))
    return result

letters = string.ascii_lowercase + string.ascii_uppercase

def bruteforce():
    for i in range(2,len(XOR_KEY)+1):
        print(i)
        for key in itertools.product(letters, repeat=i):
            key =''.join(list(key))
            print(key)
            flag = xor(encrypted_message, key)
            if r'spritz{' in flag:
                print(flag)
                print(f'XOR_KEY: {key}')
                break
                
bruteforce()
                