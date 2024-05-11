# Exercise  1
### 📄 Description
You are asked to define a Python code that, given a string,
prints a string with all of the letters shifted by 2.

For example:

- `input` = 'abc'

- `output` = 'cde'

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

```python
input = 'abc'
key = 2
output =''

for i in range(len(input)):
    output += chr(ord(input[i])+key)

print(output)
```
</details>