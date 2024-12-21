#the goal of this challenge is to leverage on the xor weaknesses.

#we can read the file first
#the file is in hex encoded, it could be good to bring it in a proper form
#we know that FF is 256, i.e., we can represent the text in a decimal format,
#where each number can be encoded in ascii
with open("../encrypted.txt", 'r') as file:
    secret_hex = file.read()

def hex2dec(text):
    res = []
    for i in range(len(text)//2):
        #get the current pair of hex
        curr = text[i*2:(i+1)*2]

        #convert to int
        res.append(int(curr, 16))

    return res

secret = hex2dec(secret_hex)

#STEP 1: Key length identification
#shift string -> it allows us the comparison
def shift(text, key_length):
    return text[key_length:] + text[:key_length]

#freq counter
#we compare the original sentence with its shifted version
#we count the amount of same charcters in the same position
def freq_counter(s1, s2):
    freq = sum([1 for (x, y) in zip(s1, s2) if x == y])
    return freq

#test over different lengths.
#the hints suggests us that the length is ~8. we look between [5, +15]
for kl in range(5, 16):
    print(f"Lenght:\t{kl}\tFreq:\t{freq_counter(secret, shift(secret, kl))}")

#the highest value is with length = 8.

#STEP 2: Cryptoanalysis
#split the corpus in 8-chars lengths
def splitter(text, key_length):
    res = []
    for i in range(key_length):
        res.append(text[i::key_length])

    return res

secret_ = splitter(secret, 8)

#we need to define a method that show us the k-th most frequent character in
#a given string
from collections import Counter
def k_char(text, k):
    #use the counter
    freq = Counter(text)

    #order
    ordered = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    return ordered[k][0]

## we can now see the top N freuqent words
#print(k_char(secret))

#we now work on the Cryptoanalysis, based on each column of the matrix M[secret//8 X 8]
#we can first assume that the most common character in each column is the space ' '.
key_sec = [k_char(secret_[0], 0), k_char(secret_[1], 0), k_char(secret_[2], 0), k_char(secret_[3], 0),
    k_char(secret_[4], 0), k_char(secret_[5], 0), k_char(secret_[6], 0), k_char(secret_[7], 0)]

#xor the key
real_key = [k ^ ord(' ') for k in key_sec]

#decode the secret
real_message = ''
for i, c in enumerate(secret):
    key_pos = i % 8
    real_message+= chr(c ^ real_key[key_pos])

print(real_message)