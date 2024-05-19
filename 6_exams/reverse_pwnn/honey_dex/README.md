# HoneyDex

### 📍 Description
Catch all pokemon (and the flag)!

### 📄 Rules
- This challenge is supposed to be solve only through static analysis.
- Do not patch this binary!
- You MUST solve the challenge by providing valid inputs.
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

## 🔑 Solution
We can use radare ,the command `iz`, to look for any useful strings in the program. We found some tip about how the flag was mirrored and i found it like that. 

<p align="center">}803998_ekoPWOOOOOLS_ereh_yllaniF{ZTIRPS

We can mirror it and i found the flag


### 🚩 Flag
```plain
SPRITZ{Finally_here_SLOOOOOWPoke_899038}
```

