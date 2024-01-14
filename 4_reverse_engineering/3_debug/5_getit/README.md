# Get it
### 📄 Description
Open and read the flag!

## 🔑 Solution
You can patch the binary by just removing the piece of code that overwrites the flag with `*` and the `remove()` function with a `nop` code.

### 🚩 Flag
```plain
SharifCTF{b70c59275fcfa8aebf2d5911223c6589}
```