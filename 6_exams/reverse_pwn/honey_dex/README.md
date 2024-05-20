# HoneyDex

### 📄 Description
Catch all pokemon (and the flag)!


### ⚙ How to run
```
./honeydex
```


### ⛔ Rules
- This challenge is supposed to be solve only through static analysis.
- Do not patch this binary!
- You MUST solve the challenge by providing valid inputs.
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We notice that the program has many characters since it is full of ASCII art, so a useful command to start with might be:
```bash
strings honeydex
```

We observe that among the Pokédex numbers, there are some important tips, many of which concern writing backward, and there is one particularly important:
```plain
TIP: Maybe [command] [file] | grep "[something]" could be very useful if you remember that command! 
```

If we combine these two tips, we can obtain the command that will print the flag backward, so we just need to reverse it and we get the flag.

```bash
strings honeydex | grep "ZTIRPS"
```

### 🚩 Flag
```plain
SPRITZ{Finally_here_SLOOOOOWPoke_899038}
```

