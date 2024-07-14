# 🔑 Write-Up

The program asks the right pin. This can be obtain either using `strings hello_world` which extracts human readable strings from executables or using `ida64` which allows us to see that there's a compare statement between the input strings and `Fl4g`. Only if the 2 strings are equal, the console prints the flag.

### 🚩 Flag

```plain
Flag{reverse_hello_world}
```