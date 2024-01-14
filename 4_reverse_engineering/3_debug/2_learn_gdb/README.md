# Learn GDB
### 📄 Description
Using a debugging tool will be extremely useful on your missions. Can you run this program in gdb and find the flag?

## 🔑 Solution
The program tells us that the flag is being read to the global variable `flag_buf` so we can just insert a breakpoint just before program exit and print it.

### 🚩 Flag
```plain
picoCTF{gDb_iS_sUp3r_u53fuL_a6c61d82}
```