# 🔑 Write-Up

Since the key is 2 chars long, we can try a bruteforce approach.
The solution provided reads the encrypted message from a file, then iterates through all possible combinations of keys within the specified length range, attempting to decrypt the message. If a decrypted message containing the string `spritz{` is found, it prints the message and the key used to decrypt it. 

### 🚩 Flag

```plaintext
spritz{no_pain_no_30}
```