# Gforce
### 📄 Description
While loosing some time on the Internet you fell on a old blog-post about
conspiracy theories...

A self proclaimed hacker attached a network capture in a comment of this post
telling that he will be `0xdeadbeef` before finishing the work.

Even if the job seems risky you can't help it, you wanna look at it...
the adventure begins...

## 🔑 Solution
```python
import base64

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8','ignore')

secret = 'SU5TQXtjMTgwN2EwYjZkNzcxMzI3NGQ3YmYzYzY0Nzc1NjJhYzQ3NTcwZTQ1MmY3N2I3ZDIwMmI4MWUxNDkxNzJkNmE3fQ=='

print(base64tostring(secret))
```

### 🚩 Flag
```plain
INSA{c1807a0b6d7713274d7bf3c6477562ac47570e452f77b7d202b81e149172d6a7}
```