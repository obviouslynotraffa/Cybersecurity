# 🔑 Write-Up

To obtain the flag, we can write the following content in the file `lvl1.txt`: AAAAA and execute the following inputs:
```python
leru()
leru()
leru()
" "
```

We need to use `leru()` three times to invoke the `leru()` function, which increments the global variable `lvl1` by one each time. By doing so, `lvl1` becomes 3, allowing me to pass the first condition in the if statement to print the flag.

### 🚩 Flag

```plaintext
spritzCTF{python}
```