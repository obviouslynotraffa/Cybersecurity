# 🔑 Write-Up

The only thing we need to do is patch the jump statements. Those that are `JNZ` (75), we change to `JZ` (74), and vice versa. Where possible, we use direct `JMP` (EB), and finally,  we can just `NOP` (90) to skip the while loops.

For further questions, refer to the `patch.diff` file.


### 🚩 Flag 

```plain
spritz{C4l4m4ru_g4Me_is_fuN!}
```