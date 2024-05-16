# Split
### 📄 Description
I'll let you in on a secret; a useful string `/bin/cat flag.txt` is present in this binary, as is a call to `system()`. It's just a case of finding them and chaining them together to make the magic happen.

### ⚙ How to run it
```bash
./split
```

### ⛔ Rules
Don't open the `flag.txt` file.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Luckily `pwntools` lib does all the hard work for us, we just need to overflow the stack up to the point where the `pwnme` return address is stored. We just need to call system with the address of the `usefulString` as an argument.


<h3> 🚩 Flag </h3>

```plain
ROPE{a_placeholder_32byte_flag!}
```
</details>