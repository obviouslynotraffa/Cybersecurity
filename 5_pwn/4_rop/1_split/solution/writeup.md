# 🔑 Write-Up

Luckily `pwntools` lib does all the hard work for us, we just need to overflow the stack up to the point where the `pwnme` return address is stored. We just need to call system with the address of the `usefulString` as an argument.

### 🚩 Flag

```plain
ROPE{a_placeholder_32byte_flag!}
```