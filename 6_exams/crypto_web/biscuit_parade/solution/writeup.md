# 🔑 Write-Up

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