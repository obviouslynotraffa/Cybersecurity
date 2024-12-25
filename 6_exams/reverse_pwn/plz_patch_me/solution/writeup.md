# 🔑 Write-Up

We can patch the binary, so:
- First input: `Y`;
- We can just change the `op code` of the to a direct jump, so: `JZ` => `JNZ`, so `74` => `75`;
- Analyzing the code, we see that the correct inputs are randomly generated at runtime. We can patch the `JZ` instructions to `JMP` in order to make the program accept every input, so `74` => `EB`
- We don't want to wait 150 seconds, so just replace `JLE` with a `NOP` so it only gets executed once (you have to do it twice).


### 🚩 Flag 

```plain
spritz{th4ts_wh4t_sh3_s41d}
```