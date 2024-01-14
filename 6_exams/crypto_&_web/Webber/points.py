#game instructions
print("Welcome to the CTF points dispatcher. In this game, the more you score, the higher your evaluation.")

#current points
pnt = 0
print(f"\nCurrent points=\t{pnt}")

def level1(x):
    try:
        x = int(x)

        if x < 10:
            score = x
        else:
            score = 1
    except:
        x_vec = x.split("7")
        if len(x_vec) == 2:
            try:
                x_vec[0] = x_vec[0][-1]
                x_vec[1] = x_vec[1][0]
                score = int(x_vec[0]) + int(x_vec[1])
            except:
                score = 2
        else:
            score = 8

    if score > 10:
        return 4
    else:
        return 0

#user input
print("\n\nLevel 1. To pass the level, you need to insert an input greater than 10")
lvl1 = input("Insert you input:\t")

#execute level 1
score_lvl1 = level1(lvl1)

#increase the points
pnt += score_lvl1
print(f"\n\nYou score=\t{score_lvl1}\ttotal points=\t{pnt}")

print("\n\nLevel 2. To pass the level, write SPRITZ")
lvl2 = input("Insert you input:\t")

def level2(x):
    #sanitization
    x = x.replace("RI", "")

    if x == "SPRITZ":
        return 4
    else:
        print("Wait, what? I think you forgot something ...")
        return 0

score_lvl2 = level2(lvl2)

#increase the points
pnt += score_lvl2
print(f"\n\nYou score=\t{score_lvl2}\ttotal points=\t{pnt}")

if pnt != 8:
    print("\n\nYou lost. To get the flag, you need to have 8 points.")
else:
    print("\n\nCOngr4t5!!! SPRITZCTF={webgame202001}")
