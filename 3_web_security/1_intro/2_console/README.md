# Console
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

Check inside `docker_run` the ip:port to use: [127.0.0.1:8081](127.0.0.1:8081).

### ⛔ Rules
You don't have access to `web` folder.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We try something in the box but nothing can help us.

We analize the js code:

We can see that first see that the value that we insert is controlled with the md5 function and, if there is a match, a function `getThat(“Y”)` is called,
otherwise `getThat(“N”)`.

So in our browser we can go in the console section, call it and the flag will appear:

<h3> 🚩 Flag </h3>

```plain
flag{console_control_js}
```
</details>