# 🔑 Write-Up

Analize the code: we see there's some usefull comment given by mistake by the developer:

>Development test account:
> * user: `JohnTestUser`
> * pass: `AtestAccount`

We try to put the info on the box and try to log and we will redirect to another page.

Seems ther's another level, we can go:
 
`Ispection >>  Application` and we change from `user` to `admin` and the flag will appear.


### 🚩 Flag

```plain
flag{C00kies_can_be_chenged?}
```