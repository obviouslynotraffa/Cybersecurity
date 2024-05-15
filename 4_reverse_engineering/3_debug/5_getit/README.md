# Get it
### 📄 Description
Open and read the flag!

### ⚙ How to run it
```bash
./getit
```
<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
You can patch the binary by just removing the piece of code that overwrites the flag with `*` and the `remove()` function with a `nop` code.

Checkout the `patch.diff` file.

<h3> 🚩 Flag </h3>

```plain
SharifCTF{b70c59275fcfa8aebf2d5911223c6589}
```
</details>