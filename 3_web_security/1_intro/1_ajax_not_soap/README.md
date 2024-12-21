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
