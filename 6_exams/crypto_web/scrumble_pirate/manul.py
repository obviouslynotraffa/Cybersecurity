

with open("challenge.txt", "r") as ciphertext_file:
    ciphertext = ciphertext_file.read().lower()
    
# Just change manually each letter

#I know the flag format so
ciphertext = ciphertext.replace("d", "S")
ciphertext = ciphertext.replace("m", "P")
ciphertext = ciphertext.replace("p", "R")
ciphertext = ciphertext.replace("x", "I")
ciphertext = ciphertext.replace("s", "T")
ciphertext = ciphertext.replace("t", "Z")


#PIRhTlS -> PIRATES
ciphertext = ciphertext.replace("h", "A")
ciphertext = ciphertext.replace("l", "E")


#wREAT -> GREAT
#TREASrRE -> TREASURE
ciphertext = ciphertext.replace("w", "G")
ciphertext = ciphertext.replace("r", "U")


#oARRATeR -> NARRATOR
ciphertext = ciphertext.replace("o", "N")
ciphertext = ciphertext.replace("e", "O")

#TaE -> THE
#PIEzE -> PIECE
ciphertext = ciphertext.replace("a", "H")
ciphertext = ciphertext.replace("z", "C")

#vOUNy -> FOUND
ciphertext = ciphertext.replace("v", "F")
ciphertext = ciphertext.replace("y", "D")


#qINK -> KING
#uEFT -> LEFT
ciphertext = ciphertext.replace("q", "K")
ciphertext = ciphertext.replace("u", "L")


#LUFFn -> LUFFY
#cORDS -> WORDS
ciphertext = ciphertext.replace("n", "Y")
ciphertext = ciphertext.replace("c", "W")


# kY -> MY
# fY -> BY
ciphertext = ciphertext.replace("f", "B")
ciphertext = ciphertext.replace("k", "M")

# gOURNEY -> JOURNEY
# 
ciphertext = ciphertext.replace("g", "J")

print(ciphertext)