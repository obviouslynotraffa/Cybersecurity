# 🔑 Write-Up

Nothing much on the page, we can check the cookies.

There are two cookies:

- `Flag{you_cant_use_this_flag}`
- UID: `df3gth4BHSGDYJhH`

the vale of UID seems to be an hashed value. If we use an online tool and md5 we can brute force to get the flag:

### 🚩 Flag

```plain
encryptCTF%7B4lwa4y5_Ch3ck_7h3_c00ki3s%7D%0A
```