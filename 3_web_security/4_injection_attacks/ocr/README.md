# OCR

### 📄 Description
OCR.
Because creating real pwn challs was to mainstream, we decided to focus on the development of our equation solver using OCR.


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

Check inside `docker_run` the ip:port to use: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

### ⛔ Rules
You don't have access to `web` folder.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

* after some trial and error it looks like the application is running an ocr on the input string and then `eval()`ing the text
* while scanning endpoints using ffuf (`ffuf -w SecLists/Discovery/Web-Content/common.txt -u http://localhost:5000/FUZZ`) a `/debug` endpoint appeared, it just dumps the app source code
* looks like the flag is in a string var named `x`
* we can't exfiltrate it directly because the output is casted to int before being sent back
* we can get the string length and then iterate on the string contents and get them character by character

<h3> 🚩 Flag </h3>

```
INSA{0cr_L0ng}
```
</details>