# Ultraencoded

### 📄 Description
Fady didn't understand well the difference between encryption and encoding,
so instead of encrypting some secret message to pass to his friend, he
encoded it!

The flag should be in the format: ALEXCTF 

## 🔑 Solution
```python
with open('zero_one.txt', 'r') as file:
    input = file.read()

input = input.replace('ZERO', '0')
input = input.replace('ONE', '1')
input = input.replace(' ', '') 

input = input.strip()

result=''.join(chr(int(input[i*8:i*8+8],2)) for i in range(len(input)//8))

import base64
decoded = base64.b64decode(result).decode('ascii')

alpha2morse = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.' }

morse2alpha = {value:key for key,value in alpha2morse.items()}

decoded2 = ''.join(morse2alpha.get(i) for i in decoded.split())
print(decoded2)
```

### 🚩 Flag
```plain
ALEXCTFTH15O1SO5UP3RO5ECR3TOTXT
```