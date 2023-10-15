
def rule9b0(b):
    #get indexed
    row = int(b[0])
    col = int(b[1:], 2)

    matrix = [['101','010', '001', '110', '011', '100', '111', '000'],
        ['001',	'100',	'110',	'010',	'000','111',	'101',	'011']
    ]

    return matrix[row][col]

def rule9b1(b):
    #get indexed
    row = int(b[0])
    col = int(b[1:], 2)

    matrix = [['100','000','110','101','111','001','011','010'],
        ['101','011','000','111','110','010','001','100']]

    return matrix[row][col]



# we need to convert the text into bits
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

    #Rule 1.
    text_bin = string2binary(text)
    if (len(text_bin) % 12 != 0):
        raise Exception(f'Rule 1 not respected.')

    #Rule 2
    key_bin = string2binary(key)
    if (len(text_bin) < 8):
        raise Exception('Rule 2 not respected')

    #rule3
    #we have some blocks ...
    for bnum in range(len(text_bin) // 12):
        i = bnum

        #define the block
        from_ = 0 + 12*bnum
        to_ = 12 * (bnum + 1)
        block = text_bin[from_:to_]

        #rule4
        for r in range(R):
            #rule5
            Lr, Rr = splitblock(block)

            #rule6
            Rr_expanded = expand_miniblock(Rr)

            #Rule7
            curr_key = key_bin[(i* R + r) : ((i* R + r)+8)]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)

            #Rule8
            Rr_exp_xor_key_0 = Rr_exp_xor_key[:4]
            Rr_exp_xor_key_1 = Rr_exp_xor_key[4:]

            #Rule9
            Rr_exp_xor_key_0_conv = rule9b0(Rr_exp_xor_key_0)
            Rr_exp_xor_key_1_conv = rule9b1(Rr_exp_xor_key_1)

            #Rule10
            Rr_sboxes = Rr_exp_xor_key_0_conv + Rr_exp_xor_key_1_conv
            if len(Rr_sboxes) != 6:
                raise Exception("Error on Rule 10")

            #Rule11
            Rr_alt = xor(Lr, Rr_sboxes)[2:]

            #Rule12
            block = Rr + Rr_alt

            #Rule13
            #end of step

        #append the result.
        text_encr += block

    return text_encr

#solution
def decrypt(text, key, R):
    text_dec = ''

    #the text is already in the bit format.
    #we only need to convert the key
    text_bin = text
    key_bin = string2binary(key)
    if (len(text_bin) < 8):
        raise Exception('Rule 2 not respected')

    #similar to the previous cycle, we need to iterate over the blocks.
    #since the blocks are independent between each other, we can use the
    #same order of the encryption algorithm
    for bnum in range(len(text_bin) // 12):
        i = bnum

        #define the block
        from_ = 0 + 12*bnum
        to_ = 12 * (bnum + 1)
        block = text_bin[from_:to_]

        #we now need to reverse the rule4 loop
        #since this time the results obtained in a specific round affect the
        #next one, we use the reverse order
        #our goal is to retrieve the original Lr and Rr
        for r in range(R-1, -1, -1):
            #in the first round we obtain the components
            # block = Lr + Rr
            Rr, Rr_alt = splitblock(block)


            #to reverse Rule11 we can use the xor properties
            #e.g.: A xor B = C, C xor B = A
            #however, we need to have one of the components at least (A or B) since
            # we have C
            # N.B. we actually have something useful. Which is Rr.
            # We know half of the info! we can wasilt obtain Rr_sboxes
            # compute from rule6 to rule10, where Lr is not involved at all
            #rule6
            Rr_expanded = expand_miniblock(Rr)
            #Rule7
            curr_key = key_bin[(i* R + r) : ((i* R + r)+8)]
            Rr_exp_xor_key = xor(Rr_expanded, curr_key)
            #Rule8
            Rr_exp_xor_key_0 = Rr_exp_xor_key[:4]
            Rr_exp_xor_key_1 = Rr_exp_xor_key[4:]
            #Rule9
            Rr_exp_xor_key_0_conv = rule9b0(Rr_exp_xor_key_0)
            Rr_exp_xor_key_1_conv = rule9b1(Rr_exp_xor_key_1)
            Rr_sboxes = Rr_exp_xor_key_0_conv + Rr_exp_xor_key_1_conv
            #Rule10
            if len(Rr_sboxes) != 6:
                raise Exception("Error on Rule 10")

            #we can finally obtain Lr
            Lr = xor(Rr_alt, Rr_sboxes)
            Lr = Lr[2:]
            block = Lr + Rr

        #obtain the new block
        new_block = Lr + Rr
        #print(new_block)
        # raise Exception('# DEBUG: ')

        #append the result.
        text_dec += new_block

    #Convert from 8digit bits into the integer, and then
    #in the ascii representation
    res = ''
    for i in range(len(text_dec) // 8):
        res += chr(int(text_dec[(i * 8): ((i+1) * 8)] ,2))
    print(res)


#print(encrypt('abc', 'Mu', 2))
puzzle = "011001010010001010001100010110000001000110000101"
key_ex = 'Mu'
R_ex = 2
#decrypt(puzzle, key_ex, R_ex)
#flag: Min0n!
decrypt(encrypt('Min0n!', 'Mu', 2), 'Mu', 2)
