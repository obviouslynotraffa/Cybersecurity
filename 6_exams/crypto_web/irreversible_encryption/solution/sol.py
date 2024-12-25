
import base64
import string
import binascii

ALPHABET = list(string.printable)   # len = 100
LEN = len(ALPHABET)

def base64encode(message):
    message_bytes = message.encode('ascii')
    b64_bytes = base64.b64encode(message_bytes)
    b64_message = b64_bytes.decode('ascii')
    return b64_message

# same for b32
def base32encode(message):
    message_bytes = message.encode('ascii')
    b32_bytes = base64.b32encode(message_bytes)
    b32_message = b32_bytes.decode('ascii')
    return b32_message

# I think I'm forgetting something important to remove here
def XORencode(message, KEY="c4mPar1"):
    rep = len(message)//len(KEY) + 1
    key = (KEY*rep)[:len(message)] # adjust the key len
    xored = ''.join([chr(ord(a) ^ ord(b)) for a,b in zip(message, key)])
    return xored

# Easy-to-use function, that looks useful
def ROTencode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i+pos)%LEN]
    return rot13_enc

# a useless method that could be replaced by a single line of code
# why not?
def ascii_to_hex(message):
    encoded = binascii.hexlify(message).decode()
    return encoded

with open("../encrypted_flag.txt", "r") as f:
    hex_encrypted=f.read()
    f.close()
    
# decode from hex to ascii
decoded = binascii.unhexlify(hex_encrypted)
decoded = decoded.decode('ascii')

# decodeteh xor
decoded = XORencode(decoded) 


#inverse the operations

for _ in range(15):
    decoded = ROTencode(decoded,-3)
    decoded = base32encode(decoded)
    decoded = ROTencode(decoded, -13)
    decoded = base64encode(decoded)
    
print(decoded)

