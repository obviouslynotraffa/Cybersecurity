# DebugMeNot

### 📄 Description
The program runs several checks to detect a debugging environment. If running into gdb, every test should FAIL. 

Patch the program to obtain PASS in every check even when running into gbd.

### ⚙ How to run it
```bash
./debugmenot
```
<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
An easy way to solve this challenge is to make all the test function return 0. 

Checkout the `patch.diff` file.

There's no flag in this challenge.
</details>