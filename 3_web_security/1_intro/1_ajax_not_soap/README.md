# Ajax not soap
### 📄 Description
Javascript is checking the login password off of an ajax call, the verification is being done on the client side.
Making a direct call to the ajax page will return the expected password.

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

Check inside `docker_run` the ip:port to use: [127.0.0.1:8085](127.0.0.1:8085).

### ⛔ Rules
You don't have access to `web` folder.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Check the javascript code. There are two main functions, one that checks the username, and one that checks the password. The correct pairs of username-passwords are retrieved using a “webhooks” ajax function.

Well, since this is a client-side control, we can use the browser debugger and set two
breakpoints on the lines that clean the data variable (i.e., `data = data.replace([...])`).

We can do the same thing for the password and the flag will appear:

<h3> 🚩 Flag </h3>

```plain
flag{hj38dsjk324nkeasd9}
```
</details>