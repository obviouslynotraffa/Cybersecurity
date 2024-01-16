# Crypto Challenge

### 📄 Description
This time you intercepted a communication between Professor Conti and his
teaching assistants. But this is encrypted!

Luckily, we know that their common encryption mechanisms is:

1. From plain message to Base64
2. Transform the Base64 with a Rotation Cipher of 13 positions

In order to read it, you need to perform the encrypting operation in reverse.

Good luck!

## 🔑 Solution

We just need to perform the encrypting operation in reverse, so:
1. Transform the Base64 with a Rotation Cipher of 13 positions
2. From plain message to Base64

and we'll get the flag

This is the ROT function
```python
def ROTdecode(message, pos):
    rot13_enc = ''
    for c in message:
        i = ALPHABET.index(c)
        rot13_enc += ALPHABET[(i - pos)%LEN]
    return rot13_enc
```


### 🚩 Flag
```plain
spritz{another_useless_encryption}
```