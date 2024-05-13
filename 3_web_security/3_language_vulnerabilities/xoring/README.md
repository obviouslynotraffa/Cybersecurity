# Xoring
### 📄 Description
Can you retrieve the flag?

### ⚙ How to run it
Be sure that the the entire folder has the right permissions.
To do it, open the terminal and write:
```bash
chmod -R +rx ./
```

To execute the exercise, do the following on the terminal:
```bash
sudo ./docker_build.sh
sudo ./docker_run.sh
```

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

If we check the code, there somenting illegible. That's called js-obfuscation, and can be easly reverted by using a online tool.

Once the code is in a clear state, we see that the pass inserted is ciphred by a xor with key=6.


We can try and hope some simmetric encryption. So go to the console and call the function `x("_NeAM+bh_saaES_mFlSYYu}nYw\u001d}", 6)` and we'll get the flag:

<h3> 🚩 Flag </h3>

```plain
iNSA{+ThisWasSimpleYouKnow+}
```
</details>