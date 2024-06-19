# UltraEncoded

### 📄 Description

We intercepted a communication between our and the other world. We are scared about that, so we ask for your help and retrieve the message.
Unluckly, the message is encrypted but we know the sender is
the eXORcist!

Can you understand what he wants?

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Since the key is 2 chars long, we can try a bruteforce approach.
The solution provided reads the encrypted message from a file, then iterates through all possible combinations of keys within the specified length range, attempting to decrypt the message. If a decrypted message containing the string `spritz{` is found, it prints the message and the key used to decrypt it. 

<h3> 🚩 Flag </h3>

```plain
spritz{no_pain_no_30}
```
</details>