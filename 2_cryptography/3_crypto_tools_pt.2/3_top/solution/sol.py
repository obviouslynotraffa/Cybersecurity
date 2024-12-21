#to solve this challenge, we can try to find some weaknesses in the
#given algoruthm
#we can debug it

import random
import sys
import time

# =============================================================================
# step 1 - set seed
# =============================================================================
cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

print('Step 1-  current time:\t', cur_time)

#note1: current time is a byte value containing a number, which will set a seed
#floating value

# =============================================================================
#  step 2 - get message
# =============================================================================
msg = 'hello'.encode('ASCII')

# =============================================================================
# step 3 - define the key
# =============================================================================
key = [random.randrange(256) for _ in msg]

#the key is a list of values = len(len of messages)
# one value for each character in the message


# =============================================================================
# step 4 - encryption
# =============================================================================
c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

#the encryption is composed by a xor between a character and a key.
#the message is the concatenation of msg + cur_time
#the key is the concatenation of the list of keys + list of 0x88



####--------RESOLUTION -----------------
#we know that |msg| = |key|, and |cur_time| = |[0x88]|
#we can use the xor property to retrieve the cur_time of the execution

#read the secret
with open("../top_secret", "rb") as f:
    secret = f.read()
print(len(secret))

#extract the encrypted current time
sec_time = secret[-len(cur_time):]
plain_time = ''.join([chr(m ^ k) for (m, k) in zip(sec_time, [0x88]*len(cur_time))])
print(f"plain time:\t{plain_time}")
#what we printed seems a correct datatime format

#we now leverage on the pseudonumber vulnerabilities ...
#the algorithm set a seed, so it is not random the generator.
random.seed(plain_time.encode("ASCII"))

#get the keys
keys_secret = [random.randrange(256) for _ in secret[:-len(cur_time)]]
plain_text = ''.join([chr(m ^ k) for (m, k) in zip(secret[:-len(cur_time)], keys_secret)])
print(plain_text)
