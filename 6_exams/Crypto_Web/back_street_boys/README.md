# BackStreetBoys
### 📄 Description
We intercepted a message from the famous band, but it's encrypted!
Please recover it, we know the encryption algorithm!

Tell me why!


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

What we need to do is basically a function that decode a Vigenère cipher:

```python
def decryption(key,encoded):
    decryptedText=''
    key_extended = (key * (len(encoded) // len(key))) + key[:len(encoded) % len(key)]
    for i in range(len(encoded)):
        encrypted_char = encoded[i]
        char_key = key_extended[i]

        offset = 97
        if encrypted_char.isalpha():
            decrypted_char = chr((ord(encrypted_char) - ord(char_key)) % 26 + offset)
            decryptedText +=decrypted_char
        else:
            decryptedText +=encrypted_char
    return decryptedText
```

<h3> 🚩 Flag </h3>

```plain
spritz{i-want-it-that-way}
```
</details>