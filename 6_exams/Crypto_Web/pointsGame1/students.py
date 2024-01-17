lvl1 = 0
def leru():
    global lvl1
    lvl1+=1
    x1 = input("What do you wanna do?\t")
    eval(x1)

x1 = input("What do you wanna do?\t")
print(eval(x1))

with open("lvl1.txt", "r") as file:
    lvl2_txt = file.read().strip()

print("LVL2 file contains:\t", lvl2_txt)
lvl2_len = len(lvl2_txt)
lvl2 = False
if lvl2_len > 4:
    tmp = 0
    for c in lvl2_txt:
        tmp += ord(c)

    tmp =  tmp % lvl2_len

    if tmp == 0:
        lvl2 = True

if lvl1 == 3 and lvl2:
    print("Flag reached: spritzCTF{python}")
else:
    print("Wrong inputs")
