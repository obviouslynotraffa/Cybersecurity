import base64


def base64tostring(text):
    return base64.b64decode(text).decode('utf-8','ignore')

#seems like a base64
secret = 'SU5TQXtjMTgwN2EwYjZkNzcxMzI3NGQ3YmYzYzY0Nzc1NjJhYzQ3NTcwZTQ1MmY3N2I3ZDIwMmI4MWUxNDkxNzJkNmE3fQ=='


print(base64tostring(secret))