import base64

def base64tostring(text):
    return base64.b64decode(text).decode('UTF-8','ignore')

secret = 'Vmxkd1NrNVhVbk5qUlZKU1ltdGFjRlJYZEhOaWJFNVhWR3RPV0dKVmJEWldiR1JyV1ZkS1ZXRXphRnBpVkVaVFYycEtVMU5IUmtobFJYQlRUVmhDTmxZeFdtdGhhelZ5WWtWYWFWSlViRmRVVlZaYVRURmFjbFpyT1ZaV2JXUTJWa1pvYTFkck1YVlVhbHBoVWxack1GUlZaRXRqVmxaMVZHMTRXRkpVUlRCWFdIQkdUbGRHY2s1VmFFOVdNWEJoV1Zkek1XSldaSFJPVm1SclZsZDRXbFJWVm5wUVVUMDk='

#we need to decode multiple time i guess
for i in range(1,11):
    
    dec = base64tostring(secret)
    print(dec)
    print('')
    secret = dec
    
#Good job ! You found the flag: INSA{TCP_s0ck3t_4n4lys1s_c4n_b3_fun!}