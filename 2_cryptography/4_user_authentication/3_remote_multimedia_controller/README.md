# Remote multimedia controller
### 📄 Description
Caasi Vosima organized a party last night to show is new high-tech house to his
friends yet something went wrong with the multimedia player and the music was
turned off.

It took some time to restart the music player and the party was like frozen for a
moment. Caasi was able to recover some information collected just before the
crash.

Help Caasi to find out what happened !

## 🔑 Solution
```python
import base64

def base64tostring(text):
    return base64.b64decode(text).decode('UTF-8','ignore')

secret = 'Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk='

for i in range(1,11):
    
    dec = base64tostring(secret)
    print(dec)
    print('')
    secret = dec
```

### 🚩 Flag
```plain
INSA{TCP_s0ck3t_4n4lys1s_c4n_b3_fun!}
```