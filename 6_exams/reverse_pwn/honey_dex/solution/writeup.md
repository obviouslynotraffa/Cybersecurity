# 🔑 Write-Up

We notice that the program has many characters since it is full of ASCII art, so a useful command to start with might be:
```bash
strings honeydex
```

We observe that among the Pokédex numbers, there are some important tips, many of which concern writing backward, and there is one particularly important:
```plain
TIP: Maybe [command] [file] | grep "[something]" could be very useful if you remember that command! 
```

If we combine these two tips, we can obtain the command that will print the flag backward, so we just need to reverse it and we get the flag.

```bash
strings honeydex | grep "ZTIRPS"
```

### 🚩 Flag
```plain
SPRITZ{Finally_here_SLOOOOOWPoke_899038}
```