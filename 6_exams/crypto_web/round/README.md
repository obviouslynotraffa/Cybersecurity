# Round

### 📄 Description
You are given a ciphertext, and the code the attacker used to produce it.

Can you reverse the algorithm to find the plaintext?


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

The encryption was done by cyclically shifting the indices of the characters by a certain number of positions, defined by the key `k`. Therefore, to decrypt the message, we simply need to shift the indices of the characters backward by `k` positions.

```python
def decrypt(cipher, k):
    verify(cipher, a)
    
    cipher = list(cipher)

    for i in range(len(cipher)):
        in_ = cipher[i]
        idx_in = a.index(in_)
        idx_out = (idx_in - k) % len(a)
        out_ = a[idx_out]
        cipher[i] = out_

    return "".join(cipher)
```

<h3> 🚩 Flag </h3>

```plain
SptrizCTF{it_was_only_a_simple_cipher}
```
</details>