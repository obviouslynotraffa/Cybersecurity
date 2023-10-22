import base64


def base64tostring(text):
    return base64.b64decode(text).decode('utf-8','ignore')

#seems like a base64
secret = 'SU5TQXtjMTgwN2EwYjZkNzcxMzI3NGQ3YmYzYzY0Nzc1NjJhYzQ3NTcwZTQ1MmY3N2I3ZDIwMmI4MWUxNDkxNzJkNmE3fQ=='


print(base64tostring(secret))
# flag: INSA{c1807a0b6d7713274d7bf3c6477562ac47570e452f77b7d202b81e149172d6a7}