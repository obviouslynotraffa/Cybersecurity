# 🔑 Write-Up

We are given some XORed hexadecimal values and need to retrieve the flag. The provided values are:

- `X1`: A known hex string.
- `X2 ⊕ X1`: XOR result of `X2` and `X1`.
- `X2 ⊕ X3`: XOR result of `X2` and `X3`.
- `FLAG ⊕ X1 ⊕ X2 ⊕ X3`: XOR result of the flag with `X1`, `X2`, and `X3`.


### Step 1: Recover `X2`
```
X2 = (X2 ⊕ X1) ⊕ X1 
```

### Step 2: Recover `X3`
```
X3 = (X2 ⊕ X3) ⊕ X2 
```

### Step 3: Recover the Flag
```
FLAG = (FLAG ⊕ X1 ⊕ X2 ⊕ X3) ⊕ (X1 ⊕ X2 ⊕ X3) 
```

### 🚩 Flag

```plaintext
spritz{keep_it_on_repeat}
```