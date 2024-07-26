# 🔑 Write-Up

We cannot patch the binary, so we can just analyze the code using ida. Here's are the valid input:
- `Disguise as the guard Mark!`: is written in plain;
- `At dawn`: is called the function `string_rev()` and then compared with "nwad tA";
- `PuncH`: the single letters are written in plain, but their checks are not in sequential order;
- `1975`: the input is moltiplied 3 times and then compared with 5925 (in hex), so we just need to 5925/3 to get the input.

### 🚩 Flag

```python
SPRITZ{EasyBye<3}
```