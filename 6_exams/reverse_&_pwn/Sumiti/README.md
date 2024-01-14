# Sumiti

### Description
Can you get the best panino in the world and the flag?s

### Rules
- You CANNOT patch the binary.
- You MUST solve the challenge by providing valid inputs.
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

## Solution
The customer id can be easly obtain with the comand `strings`, and we get `SumitiLover1234`.

Following carefully the order of variable declaration for the sandwitch name, we notice that these lead to the string “5Fna14At”. But this is just the order in which the single char's are checked, so it's not our plain password. To get it, we need to check the order of appereance in the call, and we get `F4nTa51A`.

To guess the order of the ingridients, if we inspect `create_panino()` function, we noticed that the generation of the correct input is provided by a `rand()`. What we can do is analyze the memory (using `gdb`) when it requires input, given that the generation of the order of the ingredients has already been carried out, so wen can read the numeber.

### Flag
```plain
PRITZ{TwO_EuRo_PleAs3}
```