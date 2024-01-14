# I agree
### 📄 Description
Crack the cipher: `vhixoieemksktorywzvhxzijqni`

Your clue is:

"caesar is everything. But he took it to the next level."

## 🔑 Solution
```python
import base64

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
```

### 🚩 Flag
```plain
theforceisstrongwiththisone
```