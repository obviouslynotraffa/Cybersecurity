# CrossTheBridge

### 📄 Description
Can you cross the bridge and get the flag?

### ⚙ How to run
```bash
./CrossTheBridge
```

### ⛔ Rules
- You must not patch the `play_game_no_patch()` function, nor delete it, and this function must be executed to get the flag.
- The rest of the binary can be patched in any way you like!

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

There's a function that checks if the user has cheated using a `ptrace()` check, it can be easily patched by `NOP` the call of `stack trace`.

We see that to decide whether to generate the step L or R, it takes a random number generated by the `rand()` function and checks if it is even (% 2). What we can do is that instead of calling the rand() function, it calls a register, where the value 0 is stored. In this way, every step will always be the same: Left.

You'd better check `patch.diff` file.

<h3> 🚩 Flag </h3>

```plain
SPRITZ{WhaT_A_fUn_gAme}
```
</details>