# Ready Student One
### 📄 Description
The description of the challenge itself is on the webpage.

### ⚙ How to run
Before running anything, you need to create the database. Follow these steps:
``` bash
$ cd webapp
$ python3 db_init.py
$ export FLASK_ENV=development
$ export FLASK_APP=app
```
And run the local server with:
```bash
$ flask run
```
You should see in the command output the link to the page
If you can't find it, it should be at: http://127.0.0.1:5000/



### ⛔ Rules
In this challenge you `CANNOT` look at the `webapp` folder!

In order to get the points of this challenge, you need to provide a detailed description of the procedure that you used to get the flag.

Otherwise we account for the flag as read by the web application folder itself.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

Looking at the source code, we can see that by entering any port and a non-null IP, it takes us to a page where it says: "You choose IP d, but only `192.168.253.254` will receive the key." 

That is clearly an IP address, so we can put it in the IP box and we will get the flag at the designated IP/port.

<h3> 🚩 Flag </h3>

```plaintext
spritz{f1rst_to_the_key_f1rst_t0_th3_flag!}
```
</details>