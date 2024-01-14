#
# SW4gYmFzaCwgdG8gcmVhZCBhIGNvbnRlbnQsIHlvdSB1c2UgImNhdCBmaWxlbmFtZSIK
#

import os

#get user request
cmd = input("Enter the bash command you want execute\t")

#chunk
cmd_ch = cmd.split('&')
print(cmd_ch)

#sanitization
if "SECRET" in cmd_ch[0]:
    raise Exception("Permission denied. You cannot access the folder.")


#

#execute the command
for c in cmd_ch:
    os.system(cmd)

#str="Some string"
#printf '%s\n' "$str" | awk '{ print toupper($0) }'
