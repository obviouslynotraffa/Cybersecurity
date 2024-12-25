# 🔑 Write-Up

By performing a cryptanalysis of the code, it is observed that:

- It is checked that `msg` contains only variables of type `a`
- `msg` is transformed into a list.
- It iterates through the entire length of the message, and:
    -  The current value is taken as a character.
    - It is indexed.
    - The vulnerable part is the addition of `k`, which is used as an index to retrieve the encrypted character.
- The encrypted message is composed.

To solve this challenge we can easly create a function `decrypt()` where `k` is subtracted.

```python
def decrypt(msg, k):
    verify(msg, a)

    msg = list(msg)

    for i in range(len(msg)):
        in_ = msg[i]
        idx_in = a.index(in_)
        idx_out = (idx_in - k) % len(a)
        out_ = a[idx_out]
        msg[i] = out_

    return "".join(msg)



for k in range(-10000, 10000):
    dec = decrypt(cipher, k)
    if "SPRITZ" in dec:
        print("chiave", k)
        print(dec)
        break
```

### 🚩 Flag

```plain
SptrizCTF{it_was_only_a_simple_cipher}
```