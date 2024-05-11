# Simpledes
### 📄 Description
Larry is working on an encryption algorithm based on DES.

He hasn't worked out all the kinks yet, but he thinks it works.

Your job is to confirm that you can decrypt a message, given the algorithm and parameters used.

His system works as follows:

1. Choose a plaintext that is divisible into 12bit 'blocks'

2. Choose a key at least 8bits in length

3. For each block from i=0 while i<N perform the following operations

4. Repeat the following operations on block i, from r=0 while r<R

5. Divide the block into 2 6bit sections Lr,Rr

6. Using Rr, "expand" the value from 6bits to 8bits.
    Do this by remapping the values using their index, e.g.
    1 2 3 4 5 6 -> 1 2 4 3 4 3 5 6
7. XOR the result of this with 8bits of the Key beginning with Key[iR+r] and wrapping back to the beginning if necessary.

8. Divide the result into 2 4bit sections S1, S2

9. Calculate the 2 3bit values using the two "S boxes" below, using S1 and S2 as input respectively.

    S1	0	1	2	3	4	5	6	7
    0	101	010	001	110	011	100	111	000
    1	001	100	110	010	000	111	101	011

    S2	0	1	2	3	4	5	6	7
    0	100	000	110	101	111	001	011	010
    1	101	011	000	111	110	010	001	100

10. Concatenate the results of the S-boxes into 1 6bit value

11. XOR the result with Lr

12. Use Rr as Lr and your altered Rr (result of previous step) as Rr for any further computation on block i

13. increment r
	
	
He has encryped a message using Key="Mu", and R=2. See if you can decipher it into plaintext.

Submit your result to Larry in the format Gigem{plaintext}.

Binary of ciphertext: `01100101 00100010 10001100 01011000 00010001 10000101`

<details>
    <summary>
        <h2>🔑 Solution</h2>
    </summary>

```python

def rule9b0(b):

    row = int(b[0])
    col = int(b[1:], 2)

    matrix = [['101','010', '001', '110', '011', '100', '111', '000'],
        ['001',	'100',	'110',	'010',	'000','111',	'101',	'011']
    ]

    return matrix[row][col]

def rule9b1(b):
    row = int(b[0])
    col = int(b[1:], 2)

    matrix = [['100','000','110','101','111','001','011','010'],
        ['101','011','000','111','110','010','001','100']]

    return matrix[row][col]

def string2binary(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def binary2string(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def splitblock(block):
    Lr = block[:6]
    Rr = block[6:]
    return Lr, Rr

def expand_miniblock(b):
    return b[0] + b[1] + b[3] + b[2] + b[3] + b[2] + b[4] + b[5]

def xor(a, b):
    res = int(a, 2) ^ int(b, 2)

    return f"{res:08b}"



def encrypt(text, key, R):
    text_encr = ''

    text_bin = string2binary(text)
    if (len(text_bin) % 12 != 0):
        raise Exception(f'Rule 1 not respected.')

    key_bin = string2binary(key)
    if (len(text_bin) < 8):
        raise Exception('Rule 2 not respected')

    for bnum in range(len(text_bin) // 12):
        i = bnum

        from_ = 0 + 12*bnum
        to_ = 12 * (bnum + 1)
        block = text_bin[from_:to_]

        for r in range(R):
            Lr, Rr = splitblock(block)

            Rr_expanded = expand_miniblock(Rr)

            curr_key = key_bin[(i* R + r) : ((i* R + r)+8)]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)

            Rr_exp_xor_key_0 = Rr_exp_xor_key[:4]
            Rr_exp_xor_key_1 = Rr_exp_xor_key[4:]

            Rr_exp_xor_key_0_conv = rule9b0(Rr_exp_xor_key_0)
            Rr_exp_xor_key_1_conv = rule9b1(Rr_exp_xor_key_1)

            Rr_sboxes = Rr_exp_xor_key_0_conv + Rr_exp_xor_key_1_conv
            if len(Rr_sboxes) != 6:
                raise Exception("Error on Rule 10")

            Rr_alt = xor(Lr, Rr_sboxes)[2:]
            block = Rr + Rr_alt

        text_encr += block

    return text_encr


def decrypt(text, key, R):
    text_dec = ''

    text_bin = text
    key_bin = string2binary(key)
    if (len(text_bin) < 8):
        raise Exception('Rule 2 not respected')

    for bnum in range(len(text_bin) // 12):
        i = bnum

        from_ = 0 + 12*bnum
        to_ = 12 * (bnum + 1)
        block = text_bin[from_:to_]

        for r in range(R-1, -1, -1):

            Rr, Rr_alt = splitblock(block)

            Rr_expanded = expand_miniblock(Rr)
            
            curr_key = key_bin[(i* R + r) : ((i* R + r)+8)]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)
            
            Rr_exp_xor_key_0 = Rr_exp_xor_key[:4]
            Rr_exp_xor_key_1 = Rr_exp_xor_key[4:]
            
            Rr_exp_xor_key_0_conv = rule9b0(Rr_exp_xor_key_0)
            Rr_exp_xor_key_1_conv = rule9b1(Rr_exp_xor_key_1)
            Rr_sboxes = Rr_exp_xor_key_0_conv + Rr_exp_xor_key_1_conv
            
            if len(Rr_sboxes) != 6:
                raise Exception("Error on Rule 10")

            Lr = xor(Rr_alt, Rr_sboxes)
            Lr = Lr[2:]
            block = Lr + Rr

        new_block = Lr + Rr
        text_dec += new_block

    res = ''
    for i in range(len(text_dec) // 8):
        res += chr(int(text_dec[(i * 8): ((i+1) * 8)] ,2))
    print(res)

puzzle = "011001010010001010001100010110000001000110000101"
key_ex = 'Mu'
R_ex = 2

decrypt(encrypt('Min0n!', 'Mu', 2), 'Mu', 2)

```

<h3> 🚩 Flag </h3>

```plain
Min0n!
```

</details>