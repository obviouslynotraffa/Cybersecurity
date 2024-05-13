# Ajax not Borax
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
sudo ./docker_build.sh
sudo ./docker_run.sh
```

Check inside `docker_run` the ip:port to use: [127.0.0.1:8083](127.0.0.1:8083).

### ⛔ Rules
You don't have access to `web` folder.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>


We can analize the code. We see that if we put some breakpoints on the check of the username we can get something: 

- `c5644ca91d1307779ed493c4dedfdcb7`

We see that is coded from md5, so we can use an online tool for decode it.

If we do the same thing for the pass we'll have the flag:

<h3> 🚩 Flag </h3>

```plain
flag{sd90J0dnLKJ1ls9HJed}
```
</details>