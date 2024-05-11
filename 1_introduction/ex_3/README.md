# Exercise 3
### 📄 Description

Define a randomic password generator.
The password should contain 10 characters.

Type of characters: `alphanumeric`.

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

```python
import random
import string

len = 10
password = ''


alphanumeric = list(string.ascii_letters) + list(string.digits)

for i in range(len):
    password += alphanumeric[random.randrange(0,len(alphanumeric),1)]

print(password)
```

</details>