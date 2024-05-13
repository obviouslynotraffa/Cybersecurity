# Saltfish
### 📄 Description
"I have been told that the best crackers in the world can do this under 60 minutes but unfortunately I need someone who can do this under 60 seconds." - Gabriel


### ⚙ How to run it
Be sure that the the entire folder has the right permissions.
To do it, open the terminal and write:
```bash
chmod -R +rx ./
```

To execute the exercise, do the following on the terminal:
```bash
sudo ./docker_build.sh
sudo ./docker_run.sh
```

Check inside `docker_run` the ip:port to use: [http://127.0.0.1:124](http://127.0.0.1:124).

### ⛔ Rules
You don't have access to `data` folder.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

* `+` in php isn't string concatenation, it's just addition
* addition between two strings coerces the operands to ints
* equality between an int and a string coerces the string to an int
* first check will pass as long as:
  * `pass` is either a letter or 0
  * request user agent is the same as `pass`
* second check will pass only if the first character of `pass` is the same as the first character of `pass` concatenated with the flag.
* there are only 7 possible characters, it's trivial to bruteforce (see `solution.py`)

<h3> 🚩 Flag </h3>

```
35c3_password_saltf1sh_30_seconds_max
```
</details>