# Crypto Challenge

### 📄 Description
Provide the three input that allows you to reach the flag of the UNMODIFIED code.
In this exercise, you are free to modify the code as you wish, but
the input that you provide in the write-up must work on the original exercise version.

In the write-up, explain how you came up with those numbers.

## 🔑 Solution
To solve this exercise, it is necessary to understand the code as it is presented. The first level begins by splitting the string at the letter "a" and performs a split on it.

  -  If the string has been correctly divided into two parts, then:
    -   It takes the score and associates a number with the two pieces of the split string.
    -   Otherwise, if an exception is thrown, the score is set to 2.
- If the string is not divided:
    -    The score is set to 8.
    -    The last part checks if the score is > 180; in that case, the score is set to 4.
    -    To pass this level, simply insert a string that does not have "a" as the first/last position and you earn 4 points.

The second level takes the input as a list, changes its third character, converts it to a string, and removes 'RI' from the string. Knowing that it changes the third character, you just need to input a string that changes every third character and, therefore, allows sanitizing the string to obtain "SPRITZ." The string that satisfies this condition is `SPPRIITZ`.

### 🚩 Flag
```plain
SPRITZCTF={webgame2020_03}
```