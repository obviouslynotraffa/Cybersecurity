# 🔑 Write-Up

We just need to reverse the order of the functions, so:
1. We `XOR()` the encrypt message with the key, so we get a `32base` encryption 
2. We convert the `32base` to ascii


### 🚩 Flag

```plaintext
spritz{b4se32_is_as_secure_AS_bas364}
```