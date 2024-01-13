# Description
"One of our employees has locked himself out of his account. can you help `john galt` recover his password? 
And no snooping around his emails you hear.

## Solution
Using ida, we can see all the input the console requires:
- username: `john galt`
- password: `this-password-is-a-secret-to-everyone`

and we can easly obtain the flag.

## Flag
```plaine
TUCTF{d0n7_h4rdc0d3_p455w0rd5}
```