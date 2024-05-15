# Be quick or Be Dead
### 📄 Description
My machine is too slow for executing the program and reach the flag


### ⚙ How to run it
```bash
./be-quick-or-be-dead-1
```

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We see that the machine is too slow to get the flag. Using ida, we notice that there's a timer. What we can do is `NOP` the piece of code that sets up the timer. Check out the `patch.diff`.

<h3> 🚩 Flag </h3>

```plain
picoCTF{why_bother_doing_unnecessary_computation_27f28e71}
```

</details>