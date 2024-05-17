# Irreversible Encryption

### 📄 Description
I found a way to encrypt a message that is so efficient that from a short text creates a huuuuuuuuge file.

Finally I can communicate with my FRIENDO without
problems!
Can you find a way to reverse the operation?


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We just need to invert the operations used to encrypt the key. We can use the same functions, but call them in inverse order

```python
decoded = binascii.unhexlify(hex_encrypted)
decoded = decoded.decode('ascii')

decoded = XORencode(decoded) 

for _ in range(15):
    decoded = ROTencode(decoded,-3)
    decoded = base32encode(decoded)
    decoded = ROTencode(decoded, -13)
    decoded = base64encode(decoded)
```

<h3> 🚩 Flag </h3>

```plain
spritz{But_wait_R3versible_OP3rations_are_B4D}
```
</details>