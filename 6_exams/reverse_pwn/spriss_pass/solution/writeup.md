# 🔑 Write-Up

Using IDA, we can notice that the required password is written in plain text; however, the check on individual characters does not happen in order. The characters found are `po3l4r`, which, with a bit of creativity and context, can be rearranged into `4p3rol`.

### 🚩 Flag 

```plain
spritz{dont_drink_too_much}
```