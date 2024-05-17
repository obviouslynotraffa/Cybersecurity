# Crypto Challenge

### 📄 Description

As usual, you intercepted a communication between the Professor and his assistants.

Unfortunatly, the communication is encrypted and you can't read the content.

Still, you found the file that generated the encrypted string!

Reverse it and try do decrypt what they wrote!


<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>


We just need to reverse the order of the functions, so:
1. We `XOR()` the encrypt message with the key, so we get a `32base` encryption 
2. We convert the `32base` to ascii


<h3> 🚩 Flag </h3>

```plain
spritz{b4se32_is_as_secure_AS_bas364}
```
</details>