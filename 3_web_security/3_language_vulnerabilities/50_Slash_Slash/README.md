# 50 Slah Slash
### 📄 Description
You own the application. 
Free to use any resource you are given (e.g., you can have a look at the files contained in the 7z file).

Can you retrieve the flag?


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Troll apart, we can check the code.

If we go to `./env/bin/activate` we can see something interesting:

- `ZW5jcnlwdENURntjb21tZW50c18mX2luZGVudGF0aW9uc19tYWtlc19qb2hubnlfYV9nb29k
X3Byb2dyYW1tZXJ9Cg==`

Clearing a b64 encoding, so we can easly decode and get the flag:

<h3> 🚩 Flag </h3>

```plain
encryptCTF{comments_&_indentations_makes_johnny_a_good_programmer}
```
</details>