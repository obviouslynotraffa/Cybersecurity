import binascii

def binary_to_ascii(binary_string):
    message=''
    for c in binary_string:
        decimal_value = int(c, 2)
        character = chr(decimal_value)
        message += character
    return message
    

with open("../secret.txt", "r") as file:
    secret = file.read()
    file.close()


secret = secret.replace("y", "1")
secret = secret.replace("x", "0")
secret = secret.split(" ")


sol=""

for c in secret:
    decimal_value = int(c, 2)
    character = chr(decimal_value)
    sol += character
print(sol)