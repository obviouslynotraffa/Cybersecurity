#Sherlock has a mystery in front of him. Help him to find the flag.


sol = ""

with open("challenge.txt") as f:

    while 1:
        char = f.read(1)

     
        if(char.isupper()):
            sol += char
            
    
        if not char:
            break
    
    #print(sol)

sol=sol.replace("ZERO","0")
sol=sol.replace("ONE","1")

result=''.join(chr(int(sol[i*8:i*8+8],2)) for i in range(len(sol)//8))
print(result)

