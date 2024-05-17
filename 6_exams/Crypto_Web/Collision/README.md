# Collision
### 📄 Description
You are given the following game.
Try to decrypt the message contained in the "ciphertext" variable.
To do so, you must use the "decrypt" function.

You are free to modify the code as you wish.
We do not accept brute-forces approaches.

N.B. The solution that you provide must work with the unmodified version.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

We can notice that the algorithm is composed of:

   - An XOR function that sets a random seed and performs XOR between the x-th character of the text and a random number between 0 and 10.
   - A hash function with a fixed value of 123, where z=x, and as long as z≥ y, it subtracts y from z.
   - An encryption function that takes the current year and uses the hash function in the XOR of the text and the current year, encrypting it correctly.
   - A decryption function that considers if the seed is <= 10000, it throws an exception; otherwise, it performs XOR between the text and the hash based on the seed.

We noticed that by calling the decrypt function with a seed value that contains a piece equal to y="value" and seed, the string is always obtained: `\UUE[U@SC6}bgwh^ohcfhujkl|27:0s5p`. This is indeed the name of the exercise, so a collision (inserting the same number in the same position, it must be moved) is occurring.

Changing the `XOR` function by inserting the seed results in the same text; in fact, the function `h` is a modulo function, as it only checks the remainder and, when it is 0, returns the same string.

It can be noted that by inputting the number 10016 in the decrypt call, the algorithm returns the correct flag


<h3> 🚩 Flag </h3>

```python
SPRITZ_CTF={hash_collisions0713u5}
```
</details>