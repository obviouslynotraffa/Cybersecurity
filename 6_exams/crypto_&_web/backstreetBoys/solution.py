def decryption(key,encoded):
    decryptedText=''
    key_extended = (key * (len(encoded) // len(key))) + key[:len(encoded) % len(key)]
    for i in range(len(encoded)):
        encrypted_char = encoded[i]
        char_key = key_extended[i]

        offset = 97
        if encrypted_char.isalpha():
            decrypted_char = chr((ord(encrypted_char) - ord(char_key)) % 26 + offset)
            decryptedText +=decrypted_char
        else:
            decryptedText +=encrypted_char
    return decryptedText


encoded='ltctfd{p-peye-mp-raee-ieu}'
key='tellmewhy'
print(decryption(key, encoded))

#flag spritz{i-want-it-that-way}