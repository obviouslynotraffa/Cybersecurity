# This is Pain

### 📄 Description
Naruto finally arrive to the hide. But the person he finds is in desperate conditions.
They are having a discussion, but Naruto can't understand a word.

Can you help him to get the meaning of the message?


## 🔑 Solution
1. Having read the ciphertext file, I noticed that it consists of `Z` and `O`.
2. Replace the Z => 0 and O => 1.
3. The result was in binary code, and I converted it into characters.
4. It was encoded in base64, and I proceeded with the decoding.
5. It was a substitution cipher text file, so we need to create a dictionary to replace the old characters with the new ones.

### 🚩 Flag
```plain
spritz{shinra_tensei_everywhere}
```