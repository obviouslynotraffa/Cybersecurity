# FreezeTime

### 📍 Description
Just get the flag man

### 📄 Rules
- You can patch the binary and do whatever you want
except taking the flag directly.
- Report every step in the write-up!

## 🔑 Solution
First of all, we need to disable the anti debugger, by `NOP` the `PTRACE`,and changing a `JNE` into a `JE` that was located inside a function called  `is_policeman_here()`.

So now we can use gdb to put a breakpoint before the flag is deleted by the program. We can easly read it from the stack.



### 🚩 Flag
```plain
SPRITZ{Za_WaRuDo_348178}
```
P.S. : OH YOU ARE APPROACHING ME JOTARO?