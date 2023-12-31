#The hard drive may be corrupted, but you were able to recover a small chunk
#of text (see "book.txt").
#Scribbled on the back of the hard drive is a set of mysterious numbers. 
#Can you discover the meaning behind these numbers? 
#(1, 9, 4) (4, 2, 8) (4, 8, 3) (7, 1, 5) (8, 10, 1)
import re

keys = [(1, 9, 4), (4, 2, 8), (4, 8, 3), (7, 1, 5), (8, 10, 1)]
flag = None
with open("book.txt") as book:
    contents = book.read()
    paragraphs = [paragraph.split("\n") for paragraph in contents.split("\n\n")]
    words = list(
        map(
            lambda paragraph: list(map(lambda line: re.sub(r"[^\sa-zA-Z]", "", line).split(" "), paragraph)), paragraphs
        )
    )
    flag = " ".join(words[key[0] - 1][key[1] - 1][key[2] - 1] for key in keys)
print(flag)


