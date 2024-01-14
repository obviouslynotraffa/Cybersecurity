# Saltfish
### 📄 Description
"I have been told that the best crackers in the world can do this under 60 minutes but unfortunately I need someone who can do this under 60 seconds." - Gabriel

http://127.0.0.1:124

(use ./docker_run.sh to run the server locally)

## 🔑 Solution
* `+` in php isn't string concatenation, it's just addition
* addition between two strings coerces the operands to ints
* equality between an int and a string coerces the string to an int
* first check will pass as long as:
  * `pass` is either a letter or 0
  * request user agent is the same as `pass`
* second check will pass only if the first character of `pass` is the same as the first character of `pass` concatenated with the flag.
* there are only 7 possible characters, it's trivial to bruteforce (see `solution.py`)
### 🚩 Flag
```
35c3_password_saltf1sh_30_seconds_max
```