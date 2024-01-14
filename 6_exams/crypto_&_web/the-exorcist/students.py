#!/usr/bin/env python3

import string
import itertools

XOR_KEY='??' # can be only letters

# read the file with the encrypted message
with open('encrypted', 'r') as f:
    encrypted_message=f.read()