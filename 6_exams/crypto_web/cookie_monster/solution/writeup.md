# 🔑 Write-Up

After launching the site, you can read either "The cookie seems quite weird" or "Cookie Monster," which suggests to examin the cookies.

1. Go to `Inspect` --> `Storage` --> `Cookies`, and observe the value `04f8996da763b7a969b1028ee3007569eaf3a635486ddab211d512c85b9df8fb` under "permission." This is a `sha256` encoded hash, meaning "user."

2. Change its value from "user" to "admin" and encode it in `sha256`, resulting in `8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918`.

3. Replace the cookie value with this newly generated hash.

4. Login and we obtain the flag

### 🚩 Flag

```plain
spritz{thank_you_for_the_cookie}
```