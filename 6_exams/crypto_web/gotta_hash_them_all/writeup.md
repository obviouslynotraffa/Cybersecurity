# 🔑 Write-Up

At each step we are given a hash. What we can do is use an online tool to discover what type of hash it is (like this [one](https://www.tunnelsup.com/hash-analyzer/)), and then use another one to decrypt it (see [this](https://www.dcode.fr/) or [this](https://crackstation.net/)).

In order we have:
1. `md5`
2. `md4`
3. `SHA1-128`
4. `SHA2-256`
5. `SHA2-512`

Each hash decrypted is the input required for that step.


### 🚩 Flag

```plaintext
spritz{I_want3d_to_be_a_p0k3mon_tr4iner} 
```