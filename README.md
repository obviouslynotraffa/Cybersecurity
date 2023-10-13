# Cybersecurity guide

All you need to know for Python is here: [W3Schools](https://www.w3schools.com/python/default.asp)


# Summary
- [Intro](#intro)
- [Encoding](#encoding)


### Intro

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

<br></br>

### Encoding


To decode from binary to ASCII you can use
```
result=''.join(chr(int(binary_string[i*8:i*8+8],2)) for i in range(len(binary_string)//8))
```
where `bin` is the variable assigned to the binary string.


The `''.join()` is really common. It's better if we analyze the previous one to clarify:
  - `char()`: transform a letter from a unicode number to string
  - `int()`: convert a string to an integer. Takes as arguments the string and the base
  - `//` floor division



<br></br>
To decode from base64 to ASCII you can use

```
import base64
decoded = base64.b64decode(encoded_string).decode('ascii')
```

















