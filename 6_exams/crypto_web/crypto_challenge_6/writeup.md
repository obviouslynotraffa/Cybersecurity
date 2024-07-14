# 🔑 Write-Up

Performing a cryptographic analysis of the code:

- We have a function `keygen()` that generates a random key of order 1 between 0 and a very large number; it is used to create a gigantic number but only increases the complexity of the file.
- We have a function `mixer()` that plants a random seed and again performs an `XOR` between the message and a random number.

Attempting a simple brute-force approach, as already seen in another exercise, yields the flag in one of the iterations. For example, trying with:

```python
for k in range(5000):
    decoded = mixer(cipher, k)
    if "spritzCTF" in decoded:
        print(decoded)
```


### 🚩 Flag

```plaintext
spritzCTF{breaking_bad}
```