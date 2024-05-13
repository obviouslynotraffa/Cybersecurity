# Sweeeeeeet
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
You don't have access to `src` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Nothing much on the page, we can check the cookies.

There are two cookies:

- `Flag{you_cant_use_this_flag}`
- UID: `df3gth4BHSGDYJhH`

the vale of UID seems to be an hashed value. If we use an online tool and md5 we can brute force to get the flag:

<h3> 🚩 Flag </h3>

```plain
encryptCTF%7B4lwa4y5_Ch3ck_7h3_c00ki3s%7D%0A
```
</details>