# Ready xor not
### 📄 Description
original data: `El Psy Congroo`

encrypted data: `IFhiPhZNYi0KWiUcCls=`

encrypted flag: `I3gDKVh1Lh4EVyMDBFo=`

The flag is a composition of two names (two animals (?)).

## 🔑 Solution
```python
import base64

original_data = "El Psy Congroo"
encrypted_data = "IFhiPhZNYi0KWiUcCls="
encrypted_flag = "I3gDKVh1Lh4EVyMDBFo="

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")

enc_data = base64tostring(encrypted_data)
enc_flag = base64tostring(encrypted_flag)

key = ''.join([chr(ord(x) ^ ord(y))for x, y in zip(original_data, enc_data)])

flag = ''.join([chr(ord(x)^ord(y)) for x,y in zip(enc_flag,key)])
print(flag)

```

### 🚩 Flag
```plain
FLAG=Alpacaman
```