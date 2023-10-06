# Cybersecurity guide

All you need to know for Python is here: [W3Schools](https://www.w3schools.com/python/default.asp)


# Summary
- [Intro](#intro)


### Intro
<br/><br/>

- `chr()`: transform a letter from a unicode number to string
- `ord()`: transform a letter from a unicode string to a number 

<br/><br/>


If you need some input from terminal, you can use this

```
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--x1", type = int)
parser.add_argument("--x2", type = int)
parser.add_argument("--y", type = int)
args = parser.parse_args()
```
and than call the single argument with `args.x1`



<br/><br/>

If you wanna create a list with all ascii letter (upper and lower) and digits, you can use the following code:

```
import string
list(string.ascii_letters) + list(string.digits)
```





















