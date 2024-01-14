# Plz patch me
### Rules
- You can patch the binary and do whatever you want
except taking the flag directly (yes, it is in clear).

- Report every step in the write-up!

## Solution
We can patch the binary, so:
- First input: `Y`
- We can just change the `op code` of the to a direct jump, so: `Jz` => `JMB`
- Analyzing the code, we see that the correct inputs are randomly generated at runtime. We can patch the `JZ` instructions to `JMP` in order to make the program accept every input
- We don't want to wait 150 seconds, so just replace `JLE` with a `NOP` so it only gets executed once


### Flag
```plain
spritz{th4ts_wh4t_sh3_s41d}
```