# 🔑 Write-Up

You can patch the binary by just removing the piece of code that overwrites the flag with `*` and the `remove()` function with a `nop` code.

Checkout the `patch.diff` file.

### 🚩 Flag

```plain
SharifCTF{b70c59275fcfa8aebf2d5911223c6589}
```