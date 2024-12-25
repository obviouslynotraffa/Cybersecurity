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
with open("../ciphertext.txt", "r") as f:
    ZO_text = f.read()
    f.close()

# Solution
dictionary={'Z':'0','O':'1'}

text = replace_chars(ZO_text, dictionary)
text = text.split(" ")
message=''
for c in text:
    decimal_value = int(c, 2)
    character = chr(decimal_value)
    message += character
base64Decode = base64.b64decode(message)
dictionary_text= {'B':'s','N':'p','O':'r','R':'i','T':'t','U':'z','A':'o','W':'m','Q':'h','K':'a','E':'w','Y':'e','G':'n','S':'k','P':'v','Z':'y','X':'f','V':'d','F':'u','C':'c','J':'l','I':'g','H':'b','D':'j','L':'x'}

text_plain = replace_chars(base64Decode.decode('utf-8'), dictionary_text)
print(text_plain)

#flag spritz{shinra_tensei_everywhere}