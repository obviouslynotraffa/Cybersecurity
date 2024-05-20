# PiovegoRecipe

### 📄 Description
Can you retrieve the Piovego's most secret recipe?


### ⚙ How to run
```bash
./PiovegoRecipe
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

We can only provide valid inputs, so let's analyze the code using ida:
- `Patate-Prezzemolate`: is written in plain;
- `56`: `x0A8` => 168, but the input is multiplied by 3;
- `123`: `x7B` in dex => 123 in dec
- `Swe4T`: the string comparison checks the single letter but not in sequential order

<h3> 🚩 Flag </h3>

```plain
SPRITZ{D15gUsT!nG!!} 
```
</details>