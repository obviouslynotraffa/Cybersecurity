import numpy as np


def keygen():
    # https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html
    key = int(np.abs(np.random.randn(1))[0] * 1000)
    print(key)
    return key


def mixer(message, key):
    np.random.seed(key)
    return "".join([chr(ord(x) ^ np.random.randint(size=1, low=50, high=100)) for x in message])
