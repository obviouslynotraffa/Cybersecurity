# Sherlock
### 📄 Description
Sherlock has a mystery in front of him. Help him to find the flag.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

```python
sol = ""

with open("challenge.txt","r") as f:

    while 1:
        char = f.read(1)
        if(char.isupper()):
            sol += char
        if not char:
            break
    
sol=sol.replace("ZERO","0")
sol=sol.replace("ONE","1")

result=''.join(chr(int(sol[i*8:i*8+8],2)) for i in range(len(sol)//8))

print(result)
```

<h3> 🚩 Flag </h3>

```plain
BITSCTF{h1d3_1n_pl41n_5173}
```

</details>