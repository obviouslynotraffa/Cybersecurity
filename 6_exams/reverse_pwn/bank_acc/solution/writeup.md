# 🔑 Write-Up

The username is easly obtain since is written in plain: `UniPD_Student`.

Following carefully the order of variable declaration for the password, we notice that these lead to the string “gP01o3!v”. But this is just the order in which the single char's are checked, so it's not our plain password. To get it, we need to check the order of appereance in the call, and we get `P10v3go!`

The pin is genereate with a `rand()` function, but we can not patch the binary, so there's nothing we can do about it. Instead, what we can do is analyze the memory (using `gdb`) when it requires input, given that the generation of the pin has already been carried out, so wen can read the otp.


### 🚩 Flag 

```plain
SPRITZ{P00r_45_DuCk}
```