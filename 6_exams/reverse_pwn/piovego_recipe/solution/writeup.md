# 🔑 Write-Up

We can only provide valid inputs, so let's analyze the code using ida:
- `Patate-Prezzemolate`: is written in plain;
- `56`: `x0A8` => 168, but the input is multiplied by 3;
- `123`: `x7B` in dex => 123 in dec
- `Swe4T`: the string comparison checks the single letter but not in sequential order

### 🚩 Flag

```plain
SPRITZ{D15gUsT!nG!!} 
```