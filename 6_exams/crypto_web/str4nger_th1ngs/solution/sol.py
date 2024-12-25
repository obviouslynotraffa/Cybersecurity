import base64

def decrypt_morse_code(morse_code):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ' ': '/'
    }

    reversed_morse_dict = {v: k for k, v in morse_dict.items()}

    words = morse_code.split('   ')  # Morse code separates words with three spaces
    decrypted_text = ""

    for word in words:
        letters = word.split(' ')
        for letter in letters:
            if letter in reversed_morse_dict:
                decrypted_text += reversed_morse_dict[letter]
            else:
                decrypted_text += ' '
        decrypted_text += ' '

    return decrypted_text.strip()


def decode_base64(encoded_string):
    decoded_bytes = base64.b64decode(encoded_string)
    decoded_text = decoded_bytes.decode('utf-8')
    return decoded_text


def numbers_to_letters(numbers):
    letters = [chr(int(num) + ord('A') - 1) for num in numbers.split("-")]
    return ''.join(letters)


with open("../cyphertext.txt") as f:
    cipher = f.readlines()
    f.close()


# first i decrypt the morse code
morse_code = cipher[0]
morse_code_in_plain = decrypt_morse_code(morse_code)
print(morse_code_in_plain)

'''
GREAT  YOU VE CLEARED THE FIRST STEP  I HAD TO ENCRYPT THE MESSAGE TO PREVENT IT FROM BEING INTERCEPTED  CONTINUE TO DECRYPT
'''

#now the rest of the cyphertext seems a b64encoding
base64_enc = cipher[1]
base64_in_plain = decode_base64(base64_enc)
print(base64_in_plain)

'''
Fbzrguvat jrveq vf tbvat ba ng gur yvoenel. V znantrq gb unpx vagb n Ehffvna sbez V sbhaq ba gur yvoenel'f jrofvgr. V guvax gurl'er hfvat gur yvoenel nf n pbire sbe zber Zvaqsynlre erfrnepu. V’z tbaan tvir lbh gur pbbeqvangrf bs gur frperg cnffntr, gryy Zvxr gb pbzr urer!

45.41130017965508%2C%2011.887730729281115%2019-16-18-9-20-26%7B20-8-5%2016-12-1-14-11%E2%80%9919%203-15-14-19-20-1-14-20%209-19%2020-8-5%2011-5-25%7D 

29656C626174726F666D6F632074656720646E61206B6E696C20656874206574736170282041396C6578776A41595A593D763F68637461772F6D6F632E65627574756F792E7777772F2F3A7370747468202165697A755320796C65766F6C20796D20646E6120656D2079622064656D726F6672657020676E6F73207373656C646E65206E61206576726573656420756F79202C7261662073696874207469206564616D20657627756F792066492021736E6F6974616C75746172676E6F43
'''

#It gives us 3 different strings to decode
list_of_enc = base64_in_plain.split("\n")

secret = list_of_enc[0]
coordinate = list_of_enc[2]
hex_enc = list_of_enc[4]


# Let's start from the first
# I try to change letter based on the text
secret= "Fbzrguvat jrveq vf tbvat ba ng gur yvoenel. V znantrq gb unpx vagb n Ehffvna sbez V sbhaq ba gur yvoenel'f jrofvgr. V guvax gurl'er hfvat gur yvoenel nf n pbire sbe zber Zvaqsynlre erfrnepu. V’z tbaan tvir lbh gur pbbeqvangrf bs gur frperg cnffntr, gryy Zvxr gb pbzr urer!"

secret = secret.lower()

# I and M are ex to detect
secret = secret.replace("v", "I")
secret = secret.replace("z", "M")

#"I Mnantrq bg" could be "I managed to"
secret = secret.replace("n", "A")
secret = secret.replace("a", "N")
secret = secret.replace("t", "G")
secret = secret.replace("r", "E")
secret = secret.replace("q", "D")

secret = secret.replace("g", "T")
secret = secret.replace("b", "O")

#"TuINx" -> THINK
secret = secret.replace("u", "H")
secret = secret.replace("x", "K")

#"pOOeDINATEf" -> "COORDINATES"
secret = secret.replace("p", "C")
secret = secret.replace("e", "R")
secret = secret.replace("f", "S")

#"jEoSITE" -> "WEBSITE"
secret = secret.replace("j", "W")
secret = secret.replace("o", "B")

# "RhSSIAN" -> "RUSSIAN"
secret = secret.replace("y", "L")

#  "TEyy" -> TELL
secret = secret.replace("h", "U")

# "THEl" -> "THEY"
secret = secret.replace("l", "Y")

# "sOR" -> "FOR"
secret = secret.replace("s", "F")

# "GIiE" -> "GIVE"
secret = secret.replace("i", "V")

# "cASSAGE" -> "MASSAGE"
secret = secret.replace("c", "M")
print(secret)

'''
SOMETHING WEIRD IS GOING ON AT THE LIBRARY. 
I MANAGED TO HACK INTO A RUSSIAN FORM I FOUND ON THE LIBRARY'S WEBSITE. 
I THINK THEY'RE USING THE LIBRARY AS A COVER FOR MORE MINDFLAYER RESEARCH. 
I’M GONNA GIVE YOU THE COORDINATES OF THE SECRET MASSAGE, TELL MIKE TO COME HERE!
'''

#The second encryption are coordinates
# By looking at it carefully, it could contain a "Numbers to letters" ecncryption, where le letters are split by a "-"
number_to_letters_enc = "19-16-18-9-20-26-20-8-5-16-12-1-14-11-3-15-14-19-20-1-14-20-9-19-20-8-5-11-5-25"

number_to_letters_plain = numbers_to_letters(number_to_letters_enc)
print(number_to_letters_plain)

'''
SPRITZTHEPLANKCONSTANTISTHEKEY
'''

# we could stop here since we have the flag, but we continue in chill

#the third ecnryption seems hex
hex = "29656C626174726F666D6F632074656720646E61206B6E696C20656874206574736170282041396C6578776A41595A593D763F68637461772F6D6F632E65627574756F792E7777772F2F3A7370747468202165697A755320796C65766F6C20796D20646E6120656D2079622064656D726F6672657020676E6F73207373656C646E65206E61206576726573656420756F79202C7261662073696874207469206564616D20657627756F792066492021736E6F6974616C75746172676E6F43"
bytes_string = bytes.fromhex(hex)
ascii_string = bytes_string.decode("ASCII")
print(ascii_string)

'''
)elbatrofmoc teg dna knil eht etsap( A9lexwjAYZY=v?hctaw/moc.ebutuoy.www//:sptth !eizuS ylevol ym dna em yb demrofrep gnos sseldne na evresed uoy ,raf siht ti edam ev'uoy fI !snoitalutargnoC

'''

#the string is reversed...
ascii_string_reverse = ascii_string[::-1]
print(ascii_string_reverse)

'''
Congratulations! If you've made it this far, you deserve an endless song performed by me and my lovely Suzie! https://www.youtube.com/watch?v=YZYAjwxel9A (paste the link and get comfortable)
'''
