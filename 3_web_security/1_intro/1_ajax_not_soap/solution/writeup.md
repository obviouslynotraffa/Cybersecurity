# 🔑 Write-Up

Check the javascript code. There are two main functions, one that checks the username, and one that checks the password. The correct pairs of username-passwords are retrieved using a “webhooks” ajax function.

Well, since this is a client-side control, we can use the browser debugger and set two
breakpoints on the lines that clean the data variable (i.e., `data = data.replace([...])`).

We can do the same thing for the password and the flag will appear:


### 🚩 Flag

```plain
flag{hj38dsjk324nkeasd9}
```