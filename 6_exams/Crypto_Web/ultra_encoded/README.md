# UltraEncoded

### 📄 Description

We retrieved an important message.
However, we cannot understand the language used ...


Can you help us?

The flag is in spritzCTF{} format.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

* The provided `secret.txt` looks like it's just something encoded in base64
* The decoded contents look like they're in base64 too
* After base64 decoding `secret.txt` 15 times we get the flag

```python
for _ in range(15):
    decoded = decoded.decode("base64")
print(decoded)
```

<h3> 🚩 Flag </h3>

```plain
spritzCTF{ultraencoded}
```
</details>