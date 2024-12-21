# 🔑 Write-Up

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