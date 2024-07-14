# 🔑 Write-Up

Looks like we need to write an auto solver for a substitution cipher.
The idea behind it is determining the frequency of each letter in the ciphertext and substituting it with the letter that has the nearest frequency in the given table (see `sol.py`).


If we want, we can manually crack this challenge because we know the flag format so we know that `DMPXST` maps to `SPRITZ`, exploiting that we can manually crack a letter at a time (see `manual.py`)
### 🚩 Flag

```plaintext
SPRITZ{CONGRATZ_U_FOUND_THE_ONE_PIECE!}
```