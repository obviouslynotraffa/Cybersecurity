import base64
# it's a Vigenère Cipher
cipher = 'vhixoieemksktorywzvhxzijqni'
key = 'caesar'

shift = []

for i in range(len(key)):
    shift.append(ord(key[i]) - 97 )


sol = ''

for i in range(len(cipher)):
    ascii_number = ord(cipher[i]) - shift[i%6]
    
    if ascii_number >= ord('a'):
        sol += chr(ascii_number)
    else:
        diff = ord('a') - ascii_number - 1
        sol += chr(ord('z') - diff)
        
print(sol)