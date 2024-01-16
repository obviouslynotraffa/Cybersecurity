import random
import string


def transformation(input):
    input = list(input)
    input.append(input[0])
    input.pop(0)
    return "".join(input)


def reverse_transformation(input):
    input = list(input)
    input.insert(0, input[-1])
    input.pop()
    return "".join(input)


def encrypt(input, seed):
    input = transformation(input)
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80, 120)) for x in input]
    input = "".join(input)
    return input

###### Solution ######

with open("secret.txt", "r") as f:
    cipher = f.read()
    f.close()

def decrypt(input, seed):
    input = list(input)
    random.seed(seed)
    input = [chr(ord(x) ^ random.randint(80,120)) for x in input]
    input = ''.join(input)
    input = reverse_transformation(input)
    return input

for i in range(1000):
    plain = decrypt(cipher, i)
    if "spritz" in plain:
        print(i, plain)
