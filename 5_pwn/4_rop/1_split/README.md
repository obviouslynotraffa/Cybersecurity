# Description
I'll let you in on a secret; a useful string `/bin/cat flag.txt` is present in this binary, as is a call to `system()`. It's just a case of finding them and chaining them together to make the magic happen.

## Solution
Luckily `pwntools` lib does all the hard work for us, we just need to overflow the stack up to the point where the `pwnme` return address is stored. We just need to call system with the address of the `usefulString` as an argument.


## Flag
```plain
ROPE{a_placeholder_32byte_flag!}
```