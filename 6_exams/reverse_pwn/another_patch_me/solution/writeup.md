# 🔑 Write-Up

The only thing we need to do is patch the jump statements. Those that are `JNZ` (75), we change to `JZ` (74), and vice versa. Where possible, we use direct `JMP` (EB), and finally, for the while loops, instead of `JLE` (7E), we use `JGE` (7D) (this needs to be done twice).

For further questions, refer to the `patch.diff` file.


### 🚩 Flag 

```plain
spritz{CPP_is_great_CPP_is_life}
```