# 🔑 Solution

```python
input = 'abc'
key = 2
output =''

for i in range(len(input)):
    output += chr(ord(input[i])+key)

print(output)
```