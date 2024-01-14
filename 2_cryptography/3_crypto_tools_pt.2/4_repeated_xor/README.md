# Repeated xor
### 📄 Description
There's a secret passcode hidden in the robot's "history of cryptography" module. But it's encrypted! Here it is, hex-encoded: encrypted.txt. Can you find the hidden passcode?

Hint:
Like the title suggests, this is repeating-key XOR. You should try to find the length of the key - it's probably around 10 bytes long, maybe a little less or a little more.

#Follow the following procedure:

STEP 1: Key length identification

      #1.1 set the key length to test
      #1.2 shift the secret string by key_length
      #1.3 count the number of characters that are the same in the same position
            between the original secret and its shifterd version
      #1.4 take the highest frequency over different key length by repearing 1.1 - 1.3


STEP 2. Cryptoanalysis


## 🔑 Solution
```python
with open("encrypted.txt", 'r') as file:
    secret_hex = file.read()

def hex2dec(text):
    res = []
    for i in range(len(text)//2):
        curr = text[i*2:(i+1)*2]
        res.append(int(curr, 16))
    return res

secret = hex2dec(secret_hex)

def shift(text, key_length):
    return text[key_length:] + text[:key_length]

def freq_counter(s1, s2):
    freq = sum([1 for (x, y) in zip(s1, s2) if x == y])
    return freq

for kl in range(5, 16):
    print(f"Lenght:\t{kl}\tFreq:\t{freq_counter(secret, shift(secret, kl))}")

def splitter(text, key_length):
    res = []
    for i in range(key_length):
        res.append(text[i::key_length])

    return res

secret_ = splitter(secret, 8)


from collections import Counter
def k_char(text, k):
    freq = Counter(text)
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return ordered[k][0]

key_sec = [k_char(secret_[0], 0), k_char(secret_[1], 0), k_char(secret_[2], 0), k_char(secret_[3], 0),
    k_char(secret_[4], 0), k_char(secret_[5], 0), k_char(secret_[6], 0), k_char(secret_[7], 0)]

real_key = [k ^ ord(' ') for k in key_sec]

real_message = ''
for i, c in enumerate(secret):
    key_pos = i % 8
    real_message+= chr(c ^ real_key[key_pos])

print(real_message)
```

### 🚩 Flag
```plain
8eb31c92334eac8f6dacfbaaa5e40294a31e66e0
```
