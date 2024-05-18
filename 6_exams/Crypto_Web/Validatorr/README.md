# Validator

### 📄 Description
This time the flag is in plain text and contained in the "SECRET" folder.

Your job is to provide an input that can read the content of the file
`./SECRET/flag.txt`

You cannot modify the code / folder, i.e., you only need to find an
input that works ...

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

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


<h3> 🚩 Flag </h3>

```plain
CTF_flag{injection_is_nice6781185}
```
</details>