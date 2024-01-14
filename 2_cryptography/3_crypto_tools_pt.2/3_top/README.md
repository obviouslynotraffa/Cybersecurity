# Top
### 📄 Description
Perfectly secure. That's for sure! Or can break it and reveal my secret?

We are given a encryption script and the a file which is encrypted with it

## 🔑 Solution
```python
import random
import sys
import time

cur_time = str(time.time()).encode('ASCII')
random.seed(cur_time)

print('Step 1-  current time:\t', cur_time)

msg = 'hello'.encode('ASCII')

key = [random.randrange(256) for _ in msg]

c = [m ^ k for (m,k ) in zip(msg + cur_time, key + [0x88]*len(cur_time))]

with open("top_secret", "rb") as f:
    secret = f.read()
print(len(secret))


sec_time = secret[-len(cur_time):]
plain_time = ''.join([chr(m ^ k) for (m, k) in zip(sec_time, [0x88]*len(cur_time))])
print(f"plain time:\t{plain_time}")

random.seed(plain_time.encode("ASCII"))

keys_secret = [random.randrange(256) for _ in secret[:-len(cur_time)]]
plain_text = ''.join([chr(m ^ k) for (m, k) in zip(secret[:-len(cur_time)], keys_secret)])
print(plain_text)
```

### 🚩 Flag
```plain
34C3_otp_top_pto_pot_tpo_opt_wh0_car3s
```