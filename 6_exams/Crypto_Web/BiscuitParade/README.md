# Biscuit Parade

### 📄 Description

IN THIS CHALLENGE YOU CANNOT LOOK AT THE webapp FOLDER!

In order to get the points of this challenge, you need to provide a 
detailed description of the procedure that you used to get the flag.
Otherwise we account for the flag as read by the web application folder itself.

### 🔧 How to run

In order to run the challenge you need to set up two environmental variables

```console
$export FLASK_ENV=development
$export FLASK_APP=app
```

and run the local server with

```console
$cd webapp
$flask run
```

You should see in the command output the link to the page
If you can't find it, it should be at http://127.0.0.1:5000/

The descriprion of the challenge itself is on the webpage.

## 🔑 Solution
1. As the challenge hints, you need to do a (fake) login, but it requires a specific cookie
(hinted by the biscuit request) in order to get the flag

2. We can use the network inspector to look inside the `GET` request of the index page.
We can notice the presence of the header `set-cookie` with the value
`permission=user`

3. Now we can try to guess the right cookie that the application wants to spit out the
flag. To do that, we can check the cookie stored in the “Storage” window, at
the “Cookie” folder. We can see the same cookie of the previous step

4. The next step is to modify this cookie, creating a new one with the right-click on the
cookie and selecting “Add item”.

5. Now you have a second cookie with a (not so) random name, you just modify the
name to be the same as the older cookie and this will overwrite it with the new default
value “value

6. Now we can change the cookie value to “admin” and see if it works, trying to login in
the next step with a random username and password

7. We can use test/test as login, setting the cookie to admin and we get the flag

### 🚩 Flag
```plain
spritz{N3zuk0-cha4a4a4a4a4a4a4a4an}
```