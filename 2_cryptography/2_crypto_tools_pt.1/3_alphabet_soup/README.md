# Alphabet soup
### 📄 Description
You are given this text, can you can decipher it using semantics?

## 🔑 Solution
```python
from collections import Counter

with open('encrpyted.txt') as file:
    data = file.read()
    
voc = {'K': 'i'}
dec = ''.join(c if c not in voc else voc[c] for c in data)

voc['Q'] = 'm'
dec = ''.join(c if c not in voc else voc[c] for c in data)
    
voc['F'] = 'a'
dec = ''.join(c if c not in voc else voc[c] for c in data)

voc['W'] = 'f'
voc['A'] = 'l'
voc['I'] = 'g'
dec = ''.join(c if c not in voc else voc[c] for c in data)

voc['G'] = 'd'
dec = ''.join(c if c not in voc else voc[c] for c in data)
    

voc['P'] = 'y'
voc['D'] = 'o'
voc['T'] = 'u'
dec = ''.join(c if c not in voc else voc[c] for c in data)

voc['M'] = 'n'
dec = ''.join(c if c not in voc else voc[c] for c in data)

voc['N'] = 't'
voc['L'] = 'h'
voc['H'] = 'b'
voc['U'] = 'e'
voc['V'] = 'w'
voc['C'] = 'r'
voc['E'] = 'r'
voc['X'] = 'c'
voc['J'] = 'p'
voc['B'] = 's'
voc['S'] = 'v'

dec = ''.join(c if c not in voc else voc[c] for c in data)

print(dec)    
```

### 🚩 Flag
```plain
doingthisbyhandismorefunthananonlinetool
```