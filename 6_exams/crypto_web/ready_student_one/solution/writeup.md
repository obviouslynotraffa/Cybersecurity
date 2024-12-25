# 🔑 Write-Up

Looking at the source code, we can see that by entering any port and a non-null IP, it takes us to a page where it says: "You choose IP d, but only `192.168.253.254` will receive the key." 

That is clearly an IP address, so we can put it in the IP box and we will get the flag at the designated IP/port.

### 🚩 Flag

```plaintext
spritz{f1rst_to_the_key_f1rst_t0_th3_flag!}
```