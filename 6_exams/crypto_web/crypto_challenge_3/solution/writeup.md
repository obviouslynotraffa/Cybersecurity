# 🔑 Write-Up

Let's perform a cryptanalysis of the code:

- The first part concatenates two portions of x, specifically:
    - The first block is from the second-to-last characters (-2) to the end.
    - The second block is from the beginning to the second-to-last characters (-2).
- The second part joins the current character and i%3; this means that we add every two characters.
- The third part reverses the string by iterating in reverse.

The simplest thing to do is to literally reverse the code; in fact, by using direct reversal, we already have the string with all indices in position, and by iterating in reverse and taking every two characters, we will exactly obtain, given that the second part always performs the same operation, the original string. In fact, using: 

```python
def dec(x):
    x = ''.join([x[len(x) - i - 1] for i in range(len(x))])
    x = ''.join([chr(ord(c) - (i % 3))for i, c in enumerate(x)])
    x = x[+2:] + x[:+2]
    return x
```

We can get the flag

### 🚩 Flag

```plaintext
spritzCTF{ex1}
```