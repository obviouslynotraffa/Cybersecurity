def xor(a, b):
    return bytes(i ^ j for i, j in zip(a, b))

x1= bytes.fromhex( "b840946f97ffe078ce6581d145ff3bd86cdfd0add863fc718300" )
X2_X1_hex= bytes.fromhex( "34f5785a7e42586044a7fc15bd7eed3b1f71045f7ecc177b22e0" )
X2_X3_hex= bytes.fromhex( "f7a5269d0cf0804431df076ec7e00df66d4bc1593c99f6bfff86" )
FLAG_X1_X2_X3_hex= bytes.fromhex( "3c95c09bef751b579adff6e0eb6b69416fcb6391949f6bba01" )

x2 = xor(x1, X2_X1_hex)

x3 = xor(x2, X2_X3_hex)

FLAG = xor(X2_X1_hex, x3)

FLAG = xor(FLAG, FLAG_X1_X2_X3_hex)

print(FLAG)