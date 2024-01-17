# Scrumble Pirate

### 📍 Description
We found an evelope with a weird content. One is a piece of paper 
with a non-sense writing and an image:
- `challenge.text`
- `compass.png`

The envelope presents only a description in the ouside:
"This is the beginning of a new era, the era of the pirates!
Are you able to find the treasure with the compass and the encrypted message?"

Note: the final plaintext must have only "lowercase" letters

### 📄 Rules: 
You cannot use online tools to solve the challenge automatically.
Provide a Python solution, where you explain every consolidation you made to achieve the solution. 


## 🔑 Solution
Looks like we need to write an auto solver for a substitution cipher.
The idea behind it is determining the frequency of each letter in the ciphertext and substituting it with the letter that has the nearest frequency in the given table (see `sol.py`).


If we wanto, we can manually crack this challenge because we know the flag format so we know that `DMPXST` maps to `SPRITZ`, exploiting that we can manually crack a letter at a time (see `manual.py`)

### 🚩 Flag
```plain
SPRITZ{CONGRATZ_U_FOUND_THE_ONE_PIECE!}
```