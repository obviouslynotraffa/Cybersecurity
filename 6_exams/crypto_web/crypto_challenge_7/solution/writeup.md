# 🔑 Write-Up

The provided transformation is just taking the first letter of the string and moving it to the last place so it's easy to reverse.
The encryption is just XORing characters with a random int generated from the seed.
So we'll need to bruteforce the seed somehow
We should be able to recognize the flag due to the known format (and the guessable character set `A-Za-z0-9{}_`)

### 🚩 Flag

```plaintext
spritz{final_chall}
```