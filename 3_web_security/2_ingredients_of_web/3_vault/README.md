# Solution 

If we try to insert some random values, e.g., “test”, the application responds with a “Denied Access” page.

If the page use on a database we can try some SQL Injection by inserting :

<p align="center">' or 1=1--</p>

We'll get redirected to anothere page, if we inspect cookies we can find a string encrypted. Seems base64 so: 

<p align="center">encryptCTF{i_H4t3_inJ3c7i0n5}</p>
