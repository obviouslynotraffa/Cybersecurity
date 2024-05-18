# This is Pain

### 📄 Description
Naruto finally arrive to the hide. But the person he finds is in desperate conditions.
They are having a discussion, but Naruto can't understand a word.

Can you help him to get the meaning of the message?


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

1. After read the ciphertext file, we can notice that it consists of `Z` and `O`.
2. Replace the Z => 0 and O => 1.
3. The result is in binary code, so we can convert it into characters.
4. It's encoded in base64, so we proceed with the decoding.
5. It's a substitution cipher text file, so we need to create a dictionary to replace the old characters with the new ones.

<h3> 🚩 Flag </h3>

```plain
spritz{shinra_tensei_everywhere}
```
</details>