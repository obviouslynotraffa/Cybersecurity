# Lazy Song

### 📄 Description

A begger gave us an envelop with two letters:

- `ciphertext.txt`
- `compass.png`

He told us that he use to sing this song during CTF exercises.
Can you help us decrypt the song?

Note: the final plaintext must have only "lowercase" letters

### ⛔ Rules:

- You cannot use online tools to solve the challenge automatically.
- Provide a Python solution, where you explain every consolidation you made to achieve the solution.

Some useful python commands:

```py
#read the ciphertext text
with open("ciphertext.txt", "r") as file:
    cipher = ''.join(file.readlines())
```
