# 🔑 Write-Up

We see that the machine is too slow to get the flag. Using ida, we notice that there's a timer. What we can do is `NOP` the piece of code that sets up the timer. Check out the `patch.diff`.


### 🚩 Flag

```plain
picoCTF{why_bother_doing_unnecessary_computation_27f28e71}
```