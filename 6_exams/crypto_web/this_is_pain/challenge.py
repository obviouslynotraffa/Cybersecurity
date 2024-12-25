#!/usr/bin/env python3

import string
import base64

alphabet = list(string.ascii_uppercase)

def replace_chars(input_string, char_dict):
    result = ""
    for char in input_string:
        result += char_dict.get(char, char)
    return result

# open and read file
with open("ciphertext.txt", "r") as f:
    ZO_text = f.read()
    f.close()
