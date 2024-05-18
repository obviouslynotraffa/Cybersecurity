import random

flag_cipher = "ye}GTE{tkspu~1"

def enc(x):
    x = x[-2:] + x[:-2]
    x = ''.join([chr(ord(c) + (i % 3))for i, c in enumerate(x)])
    x = ''.join([x[len(x) - i - 1] for i in range(len(x))])
    return x
    
