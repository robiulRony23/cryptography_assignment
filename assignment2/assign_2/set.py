import re

chk = "ci ffie-heh"


rslt2 = re.split(',|.|-|!', chk)
rslt = re.split(r'[.,?\-()\s!]', chk)
res = re.split(',| |_|-|!', chk)


print(rslt)
print(res)
print(rslt2)
