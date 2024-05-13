# Vault
### 📄 Description
Can you retrieve the flag?

### ⚙ How to run it
Be sure that the the entire folder has the right permissions.
To do it, open the terminal and write:
```bash
chmod -R +rx ./
```

To execute the exercise, do the following on the terminal:
```bash
sudo docker-compose up
```

### ⛔ Rules
You don't have access to `src` and `dump` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

If we try to insert some random values, e.g., “test”, the application responds with a “Denied Access” page.

If the page use on a database we can try some SQL Injection by inserting :

`' OR 1=1 --`

We'll get redirected to anothere page, if we inspect cookies we can find a string encrypted. Seems base64 so: 

<h3> 🚩 Flag </h3>

```plain
encryptCTF{i_H4t3_inJ3c7i0n5}
```
</details>