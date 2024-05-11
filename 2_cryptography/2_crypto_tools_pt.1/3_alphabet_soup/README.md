# Alphabet soup
### 📄 Description
You are given this text, can you can decipher it using semantics?

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

```python
from collections import Counter

with open('encrpyted.txt') as file:
    data = file.read()
    
# K is alone, could be 'I'
voc = {'K': 'i'}
dec = ''.join(c if c not in voc else voc[c] for c in data)


# Q could be 'm'
voc['Q'] = 'm'
dec = ''.join(c if c not in voc else voc[c] for c in data)
    
# F is alone, could be 'a'
voc['F'] = 'a'
dec = ''.join(c if c not in voc else voc[c] for c in data)


# seems 'flag'
voc['W'] = 'f'
voc['A'] = 'l'
voc['I'] = 'g'
dec = ''.join(c if c not in voc else voc[c] for c in data)


# gig could be 'did'
voc['G'] = 'd'
dec = ''.join(c if c not in voc else voc[c] for c in data)
    
    
# PDT -> 'you'
voc['P'] = 'y'
voc['D'] = 'o'
voc['T'] = 'u'
dec = ''.join(c if c not in voc else voc[c] for c in data)

# goiMg seems 'going'
voc['M'] = 'n'
dec = ''.join(c if c not in voc else voc[c] for c in data)


# trying to fill the word with right letters
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

<h3> 🚩 Flag </h3>

```plain
doingthisbyhandismorefunthananonlinetool
```
</details>