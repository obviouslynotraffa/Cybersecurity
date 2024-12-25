# 🔑 Write-Up

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



### 🚩 Flag

```plaintext
spritz{But_wait_R3versible_OP3rations_are_B4D}
```