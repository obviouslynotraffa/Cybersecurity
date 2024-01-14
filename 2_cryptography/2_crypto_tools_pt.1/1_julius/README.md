# Julius
### 📄 Description
Julius,Q2Flc2FyCg==

World of Cryptography is like that Unsolved Rubik's Cube, given to a child that has no idea about it.
A new combination at every turn.

Can you solve this one, with weird name?

ciphertext: fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ==

## 🔑 Solution
```python
import base64

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")

enc64 = 'Q2Flc2FyCg=='
decoded = base64tostring(enc64)

puzzle = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='

decoded2 = base64tostring(puzzle)

def brute_force_caesar(text):
    for i in range(-30,30):
        sol = ''.join([chr(ord(c) + i) for c in text])
        print(sol)

brute_force_caesar(decoded2)
```

### 🚩 Flag
```plain
ecCTF3T_7U_BRU73?!
```
