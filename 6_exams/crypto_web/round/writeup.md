# 🔑 Write-Up

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

### 🚩 Flag

```plaintext
SptrizCTF{it_was_only_a_simple_cipher}
```