# 🔑 Write-Up

First of all, we need to disable the anti debugger, by `NOP`ing the `PTRACE`, (see `patch.diff`).

So now we can use gdb to put a breakpoint before the flag is deleted by the program. We can easly read it from the stack.


### 🚩 Flag

```plain
SPRITZ{Za_WaRuDo_348178}
```
P.S. : OH YOU ARE APPROACHING ME JOTARO?
