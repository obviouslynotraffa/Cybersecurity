# FreezeTime

### 📄 Description
Just get the flag man

### ⚙ How to run
```bash
./freezeTime
```

### ⛔ Rules
- You can patch the binary and do whatever you want
except taking the flag directly.
- Report every step in the write-up!

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

First of all, we need to disable the anti debugger, by `NOP`ing the `PTRACE`, (see `patch.diff`).

So now we can use gdb to put a breakpoint before the flag is deleted by the program. We can easly read it from the stack.



<h3> 🚩 Flag </h3>

```plain
SPRITZ{Za_WaRuDo_348178}
```
P.S. : OH YOU ARE APPROACHING ME JOTARO?

</details>