# Points Game

### 📄 Description
Provide the three input that allows you to reach the flag of the UNMODIFIED code.
In this exercise, you are free to modify the code as you wish, but
the input that you provide in the write-up must work on the original exercise version.

In the write-up, explain how you came up with those numbers.


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

At the first level, we need to enter a string where the digit 7 is inside, and the letter before and after 7 is added together. If this sum is greater than 10, we score enough points.

The second step can be passed by exploiting the fact that `str.replace` in python doesn't recursively replace stuff using the input `SPPRIITZ`

<h3> 🚩 </h3>

```plain
SPRITZCTF={webgame202001}
```
</details>