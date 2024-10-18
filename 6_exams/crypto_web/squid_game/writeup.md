# 🔑 Write-Up

The context of the challenge and the text on the site suggest looking at the cookies. So we go to:

`Inspect` --> `Storage` --> `Cookies` 

We observe that there is a single entry called `permission`, with the value `user`. All we need to do is change it from user to `admin`. Any combination of password and username will lead us to the flag.

### 🚩 Flag

```plain
spritz{SweetVictory123}
```