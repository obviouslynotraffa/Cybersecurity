# collegeAdmission
### 📍 Description
Can you get accepted to the Eden's College?

### 📄 Rules
- If you want, you can patch this binary!
- Don't change/remove the auxil file.
- YOU CANNOT PATCH THE MAIN FUNCTION!!!
- You CANNOT just jump with the debugger to any function that directly prints the flag.
- If you think you're breaking these rules with your solution, please ask the teachers.

## 🔑 Solution
For the first question, we can see with ida that the correct input is: `Anya Forger, Park Avenue 128`. 

The second and the third question is asked to enter a digit from 0 to 9, where the correct answer is always different. This result, is decided in `think()` function, that use a `rand()` to have random numbers. What we can do is `nop` the piece of code where the `seed` of the `rand()` is set, so the `rand()` return always the same value.

### 🚩 Flag
```plain

```