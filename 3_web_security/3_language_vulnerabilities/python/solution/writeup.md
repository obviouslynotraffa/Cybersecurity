# 🔑 Write-Up

We need to insert an IP and a Port in order to do something, i.e., reach the flag. In addition, the
app contains a source (see the link): if we open it, we can see a Python code. Let’s copy this
code in local and try to figure it out what it’s doing.


Clearing the code we can see that the print uses the format `%(allowed_ip)s` for printing the value contained in the dictionary, so we can use that in the form and get the flag:

### 🚩 Flag

```plain
INSA{Y0u_C@n_H@v3_fUN_W1Th_pYth0n}
```