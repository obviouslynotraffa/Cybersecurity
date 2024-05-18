#Try to reverse the proposed encryption algorithm to reveal the flag contained
#in the "SECRET" folder.
#The flag is SRPIWS_AVF>relarzytkmn4<3671~

plaintext = "SRPIWS_AVF>relarzytkmn4<3671~"
key = 'password'

import random
import datetime

def some_fancy_struggling_function(n):
    if n<=0:
        raise Exception("Incorrect input")
    elif n==1: 
        return 0
    elif n==2:
        return 1
    else:
        return (some_fancy_struggling_function(n-1) + some_fancy_struggling_function(n-2))

def hello_world(a, b, c):
    for i in range(c):
        a = a ^ b
    return a


def most_secure_encryption_of_the_world(plaintext, key):
    w = len(key) #length of the key
    plaintext_not_so_plain = [ord(x) for x in (plaintext)] #Convert the plaintext to a list of ASCII values
    print(plaintext_not_so_plain)
    definitely_not_a_plain_text = []
    for i, x in enumerate(plaintext_not_so_plain):
        idx = i % len(key) #Get the index of the key
        definitely_not_a_plain_text.append(chr(hello_world(x, w, idx))) #Apply the encryption algorithm
    return definitely_not_a_plain_text

ciphertext=most_secure_encryption_of_the_world(plaintext, key)

#save the message
with open('./enc_message.txt', 'w') as file:
    file.writelines(ciphertext)

