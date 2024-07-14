# 🔑 Write-Up

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

```plaintext
spritz{another_useless_encryption}
```