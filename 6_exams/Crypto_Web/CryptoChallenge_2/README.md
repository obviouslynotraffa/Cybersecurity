# Crypto Challenge

### 📄 Description
Use the interface provided in students.py to retrieve the content of the flag.
Your write-up must contain an input that allows to reach the flag.

## 🔑 Solution
Looking at the file `challenge.py`, it can be seen that the program takes any string as input and executes it in the terminal without performing checks to allow only a "ping." Therefore, it is possible to concatenate other instructions to be executed in the terminal using the `|` command, checking where the flag is located by using as input:

```bash
127.0.0.1 | ls
```

We can find the file `flag.txt`, and by executing

```bash
127.0.0.1 | cat flag.txt
```

We'll find the flag

### 🚩 Flag
```plain
SpritzCTF{you_hacked_me}
```