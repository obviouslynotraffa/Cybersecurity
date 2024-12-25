# 🔑 Write-Up

The first level checks if the sum of the ascii values of the two characters around an `a` is > 180.
It looks like the input `zaz` satisfies this condition.
The second level is a little bit trickier, it changes the third letter of the input with the letter that's two letter before it in the alphabet and then it removes `RI` from the string.
The first step of the second level is passed with the input `SPPITZ`
The second step can be passed by exploiting the fact that `str.replace` in python doesn't recursively replace stuff using the input `SPPRIITZ`

### 🚩 Flag

```plaintext
SPRITZCTF={webgame2020_03}
```