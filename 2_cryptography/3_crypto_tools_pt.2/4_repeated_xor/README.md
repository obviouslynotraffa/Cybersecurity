# Repeated xor

### 📄 Description
There's a secret passcode hidden in the robot's "history of cryptography" module. But it's encrypted! Here it is, hex-encoded: `encrypted.txt`. Can you find the hidden passcode?

Hint:
Like the title suggests, this is repeating-key XOR. You should try to find the length of the key - it's probably around 10 bytes long, maybe a little less or a little more.

Follow the following procedure:

STEP 1: Key length identification

- Set the key length to test;
- Shift the secret string by `key_length`;
- Count the number of characters that are the same in the same position between the original secret and its shifterd version;
- Take the highest frequency over different key length by repearing 1 - 3.


STEP 2: Cryptoanalysis.
