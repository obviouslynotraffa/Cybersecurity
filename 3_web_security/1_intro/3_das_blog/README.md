# Das blog
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

Check inside `docker_run` the ip:port to use: [127.0.0.1:8084](127.0.0.1:8084).

### ⛔ Rules
You don't have access to `web` and `other` folders.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Analize the code: we see there's some usefull comment given by mistake by the developer:

>Development test account:
> * user: `JohnTestUser`
> * pass: `AtestAccount`

We try to put the info on the box and try to log and we will redirect to another page.

Seems ther's another level, we can go:
 
`Ispection >>  Application` and we change from `user` to `admin` and the flag will appear.


<h3> 🚩 Flag </h3>

```plain
flag{C00kies_can_be_chenged?}
```
</details>