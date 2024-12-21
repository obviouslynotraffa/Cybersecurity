# 🔑 Write-Up

If we check the code, there somenting illegible. That's called js-obfuscation, and can be easly reverted by using a online tool.

Once the code is in a clear state, we see that the pass inserted is ciphred by a xor with key=6.


We can try and hope some simmetric encryption. So go to the console and call the function `x("_NeAM+bh_saaES_mFlSYYu}nYw\u001d}", 6)` and we'll get the flag:

### 🚩 Flag

```plain
iNSA{+ThisWasSimpleYouKnow+}
```