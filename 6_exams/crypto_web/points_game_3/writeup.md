# 🔑 Write-Up

At the first level, we need to enter a string where the digit 7 is inside, and the letter before and after 7 is added together. If this sum is greater than 10, we score enough points.

The second step can be passed by exploiting the fact that `str.replace` in python doesn't recursively replace stuff using the input `SPPRIITZ`

### 🚩 Flag

```plaintext
SPRITZCTF={webgame202001}
```