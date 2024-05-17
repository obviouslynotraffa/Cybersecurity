# Crypto Challenge

### 📄 Description
We retrieved an important message.
However, we cannot understand the language used ...
can you help us?

We know the attacker generated a random key with keygen, and then he used
the mixer function to encrypt it. 

The flag is in spritzCTF{} format.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

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


<h3> 🚩 Flag </h3>

```plain
spritzCTF{breaking_bad}
```
</details>