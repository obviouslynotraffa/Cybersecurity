# another patch me

### Description
This is your CPP exam, can you pass it?

You can (must) patch this challenge

### ⚙ How to run
```bash
./another_patch_me
```

### ⛔ Rules
- You can patch the binary and do whatever you want

- Report every step in the write-up!

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

The only thing we need to do is patch the jump statements. Those that are `JNZ` (75), we change to `JZ` (74), and vice versa. Where possible, we use direct `JMP` (EB), and finally, for the while loops, instead of `JLE` (7E), we use `JGE` (7D) (this needs to be done twice). For further questions, refer to the `patch.diff` file.


<h3> 🚩 Flag </h3>

```plain
spritz{CPP_is_great_CPP_is_life}
```
</details>