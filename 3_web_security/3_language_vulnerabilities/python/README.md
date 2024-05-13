# Python
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


### ⛔ Rules
You don't have access to `www` folder.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We need to insert an IP and a Port in order to do something, i.e., reach the flag. In addition, the
app contains a source (see the link): if we open it, we can see a Python code. Let’s copy this
code in local and try to figure it out what it’s doing.


Clearing the code we can see that the print uses the format `%(allowed_ip)s` for printing the value contained in the dictionary, so we can use that in the form and get the flag:

<h3> 🚩 Flag </h3>

```plain
INSA{Y0u_C@n_H@v3_fUN_W1Th_pYth0n}
```
</details>