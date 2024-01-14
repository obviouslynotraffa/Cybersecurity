import base64

def base64tostring(text):
    return base64.b64decode(text).decode('utf-8', errors="ignore")

#first hint cryoted
enc64 = 'Q2Flc2FyCg=='
decoded = base64tostring(enc64)
#print(decoded)

#the hint says "Ceasar"

puzzle = 'fYZ7ipGIjFtsXpNLbHdPbXdaam1PS1c5lQ=='

decoded2 = base64tostring(puzzle)
#print(decoded2)



def brute_force_caesar(text):
    for i in range(-30,30):
        sol = ''.join([chr(ord(c) + i) for c in text])
        print(sol)


brute_force_caesar(decoded2)