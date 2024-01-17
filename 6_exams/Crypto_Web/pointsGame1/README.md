# Points Game

### 📄 Description
Provide the three input that allows you to reach the flag of the UNMODIFIED code.
In this exercise, you are free to modify the code as you wish, but
the input that you provide in the write-up must work on the original exercise version.

In the write-up, explain how you came up with those numbers.

## 🔑 Solution
To obtain the flag, we can write the following content in the file `lvl1.txt`: AAAAA and execute the following inputs:
```python
leru()
leru()
leru()
" "
```

We need to use `leru()` three times to invoke the `leru()` function, which increments the global variable `lvl1` by one each time. By doing so, `lvl1` becomes 3, allowing me to pass the first condition in the if statement to print the flag.

### 🚩 Flag
```plain
spritzCTF{python}
```