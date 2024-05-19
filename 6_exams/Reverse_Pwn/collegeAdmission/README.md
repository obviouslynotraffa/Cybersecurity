# collegeAdmission
### 📄 Description
Can you get accepted to the Eden's College?

### ⚙ How to run
```bash
./collegeAdmission
```

### ⛔ Rules
- If you want, you can patch this binary!
- Don't change/remove the auxil file.
- YOU CANNOT PATCH THE MAIN FUNCTION!!!
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

For the first question, we can see with ida that the correct input is: `Anya Forger, Park Avenue 128`. 

The second and the third question is asked to enter a digit from 0 to 9, where the correct answer is always different. This result, is decided in `think()` function, that use a `rand()` to generate random numbers. What we can do is `nop` the piece of code where the `seed` of the `rand()` is set (so nop the `srand()`), in this way the `rand()` function return always the same value each time we start the program. So, what we can do is a brute force approach, manually trying each number. Once the dish or video number is found, it will remain fixed even after restarting the program. Worst case scenario, you have to try 20 times.

With this patch, see `collegeAdmission_patched`, the numbers were 3 - 6 .

Before we do that, there's the anti debugger thar will check if we are patching the code or using a debugger. Since we need to disable it, we can just `nop` the call of `stack trace` in the function `security_check()`.

<h3> 🚩 Flag </h3>

```plain
SPRITZ{Ez_D3J4Vu?!?!}
```

```ascii
⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⢷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣬⣷⣘⣧⣤⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠋⢁⣢⠿⠛⠛⠻⣦⡀⠀⡉⠳⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⡄⠈⣾⠋⢀⠂⠌⡐⠘⣷⠀⡀⠄⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣶⡿⢫⠔⠂⢀⣼⠟⣀⠂⠈⠠⠐⠈⠙⢷⣄⠀⠀⠀⢿⣷⣶⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣯⡟⢰⠆⠀⢀⡾⠃⣸⡇⠀⠌⣀⠀⠀⠠⠀⠙⢷⡀⠀⠈⢻⣻⣽⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣯⡿⢀⡿⠀⠀⣾⠃⠀⣿⠀⢘⠀⠀⣿⠀⠀⢦⡀⠈⢻⣄⠀⠈⣷⢿⡾⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⢁⣼⠇⠀⣸⡏⢰⡇⣿⡆⢘⠀⠀⠹⣧⠀⠈⣷⡀⠀⢻⣄⠀⢻⣬⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⣸⣿⠀⢀⣿⢀⣼⣇⡿⣧⢸⣇⣇⠀⢻⣧⡀⠘⣿⣠⠀⣿⠀⢸⣿⡟⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⠁⣿⣹⠀⢰⣿⣾⣿⣿⣿⣾⣧⣻⣿⣦⣀⣻⣿⣶⣿⣹⣦⢸⡇⢘⣯⡇⢻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⠰⢿⣸⡅⢸⣿⣿⣟⣿⣿⣿⡍⠙⢧⠈⠉⢻⡟⢻⣿⣿⣿⣿⣗⢈⣿⣇⢉⣿⠳⣄⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⡼⣿⡇⠠⠹⣿⡇⣾⣿⠡⣿⣿⣿⣿⠀⠀⠀⠀⠀⠘⣿⣾⣿⣿⣿⣿⣿⣸⣿⡇⢂⠼⣧⠉⣝⠳⢦⣤⣀⠴⡆
⠀⠀⠀⠀⢀⣾⣷⣿⠇⢸⠁⢻⣿⣼⣿⡀⠻⣿⡿⠏⠀⠀⠀⠀⠀⠀⠸⣿⣿⡿⢠⡟⢹⣿⣻⠇⣡⢊⢹⣷⡘⢿⣦⣴⡶⠛⠀
⠀⠀⠀⢠⣾⣿⣿⣿⡎⣽⠂⠄⠻⣯⢧⠀⠐⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠠⠖⠋⢀⣿⣿⡟⣀⠲⡈⢼⣿⣿⣞⣯⠁⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣿⣿⣧⢻⡇⠌⠠⠙⢿⣷⡀⠀⠙⠲⢤⣤⣀⣀⣠⣤⠴⠚⠀⠀⢀⣾⣿⡟⠠⡄⢣⡑⣾⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⣿⣿⡿⣿⣿⣿⣼⣿⣌⢑⡈⠄⡙⢷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⡿⢈⡕⡘⠄⣾⣿⣿⣿⣿⡿⠀⠀⠀⠀
⠀⠀⠀⠈⠻⣷⡹⢿⣿⣷⢿⣿⣆⡘⢠⠁⠌⢻⣷⣶⡶⣤⣤⣤⣤⣶⣶⣿⣿⣿⣿⣿⠇⠲⣌⢂⣿⣿⣿⣿⣟⣿⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠀⠙⣿⣿⡿⣿⣿⣶⣌⡌⠤⢿⡉⠻⣦⣉⣬⡿⠯⠙⢿⣿⣿⣿⣿⢈⣱⣶⣿⣿⠟⣼⣿⠋⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣨⣿⣿⣿⣿⣿⣿⣿⣶⡼⡇⠀⣴⡿⣷⣄⠀⠀⣸⣿⣿⣿⣯⣶⣿⣿⣏⣀⡼⠟⠁⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣷⡁⠙⢻⣷⣿⡷⣾⣿⣗⠂⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣼⣿⣯⣿⣤⣼⣯⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀
⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀
⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠛⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
```
</details>