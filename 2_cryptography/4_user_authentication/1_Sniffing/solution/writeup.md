# 🔑 Write-Up

The hint suggest the usage of Wireshark.

We first filter the packets by http (see the bar with "App a display filter").
As filter, type `http`.

We reduced the traffic. In this small set of packets, we can see some request
of authentications (Info "GET / HTTP/1.1.").
One of these contain has been accepted (see its following packet).
By inspecting the "Hypertext transfer protocol", we can notice the Authorization
field. Here it contains our flag inside the credentials:

### 🚩 Flag

```plain
bashNinja:flag{help-me-obiwan}
```