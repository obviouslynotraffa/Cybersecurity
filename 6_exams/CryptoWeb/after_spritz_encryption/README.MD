# After SPRITZ Encryption

### 📄 Description

Try to reverse the proposed encryption algorithm to reveal the flag contained
in the "SECRET" folder. 


### ⛔ Rules
Don't open the `SECRET` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
The algorithm `most_secure_encryption_of_the_world` does absolutely nothing; literally, it returns the same input string, considering the following steps:

    - I obtain the length of the key;
    - I iterate through the plain text;
    - The index modulo the length of the key is always the same;
    - I return the plain text.

We note, trivially, that it is necessary to enter a password; by taking the content of the binary file and entering the password `spritz`, we retrieve the flag.

<h3> 🚩 Flag </h3>

```plain
SPRITZ_CTF={encryption753451}
```
</details>