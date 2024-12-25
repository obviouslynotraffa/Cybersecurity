# 🔑 Write-Up

The algorithm `most_secure_encryption_of_the_world` does absolutely nothing; literally, it returns the same input string, considering the following steps:

    - I obtain the length of the key;
    - I iterate through the plain text;
    - The index modulo the length of the key is always the same;
    - I return the plain text.

We note, trivially, that it is necessary to enter a password; by taking the content of the binary file and entering the password `spritz`, we retrieve the flag.

### 🚩 Flag

```plain
SPRITZ_CTF={encryption753451}
```