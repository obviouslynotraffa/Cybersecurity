# 🔑 Write-Up

If we try to insert some random values, e.g., “test”, the application responds with a “Denied Access” page.

If the page use on a database we can try some SQL Injection by inserting :

`' OR 1=1 --`

We'll get redirected to anothere page, if we inspect cookies we can find a string encrypted. Seems base64 so: 


### 🚩 Flag

```plain
encryptCTF{i_H4t3_inJ3c7i0n5}
```