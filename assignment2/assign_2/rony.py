import re
from pytrie import StringTrie 


f = open('input22.txt', 'r')
ara = []
while True:
    l = f.readline();
    if (len(l) == 0):
        break
    temp = ''
    for x in l:
        if ((x >= '0' and x <= '9') or x == ' '):
            temp += x;
    tem = [(int(i)) for i in temp.split()]
    ara += [tem];

rslt = []


def isValid(k, pos):
    flg = 0
    pre = 0
    for j in range(0, 10):
        if (pos == 0):
            pre = 0;
        else:
            pre = ara[j][pos - 1]

        tmp = (pre + k) % 256

        t = chr(ara[j][pos] ^ tmp)

        if (t >= 'a' and t <= 'z') or (t >= 'A' and t <= 'Z') or t == ' ' or t == ',' or t == '?' or t == '.' or t == '!' or t == '-' or t == '(' or t == ')':
            flg += 1
        else:
            break
    if (flg == 10):
        return True
    return False


allpos = []


def keyfind(rslt, allpos):
    for pos in range(0, 60):
        tst = []
        chk = 0
        for i in range(0, 256):
            if isValid(i, pos) == True:
                chk += 1
                if chk == 1:
                    rslt += [i]

                tst += [i]
        allpos += [tst]


keyfind(rslt, allpos)

# rony = 1
# rar = []
# for i in allpos:
#     print(i)
#     rar+=[len(i)]
#     rony*=len(i)
# print(rar)
# print(rony)


msg = ['', '', '', '', '', '', '', '', '', '']


def decode(key):
    mg = ['', '', '', '', '', '', '', '', '', '']

    for i in range(0, 60):
        pre = 0
        for j in range(0, 10):
            if i == 0:
                pre = 0
            else:
                pre = ara[j][i - 1]

            mg[j] += chr(ara[j][i] ^ ((pre + key[i]) % 256))
    global msg
    msg = mg


decode(rslt)

print("\nInitial assumed message..........\n")
for i in msg:
    print(i)
print("\n-----------------------------------------\n")

dict = []
f = open("word.txt",'r')
while True:
    inn = f.readline()
    if(len(inn)==0):
        break
    dict+=[inn[0:len(inn)-1]]
f.close()

dictList = {}
dictList = set(dict)

tri = StringTrie()

for i in dict:
    tri[i]=i


def checkDict(msg2):

    cnt = 0
    preck = ['', '', '', '', '', '', '', '', '', '']
    for i in range(0,len(msg2)):
        msg = msg2[i]
        msg3 = msg.lower()
        msg3 = prepart[i]+msg3

        #wordarr = re.split(',|\.|\?|-|!| |\(|\)', msg3)
        wordarr = re.split(r'[.,?\-()\s!]', msg3)
        # print(wordarr)
        f = 0
        for j in range(0,len(wordarr)-1):
            if(wordarr[j]==''):
                continue
            if wordarr[j] in dictList:
                f=1
            else:
                f=0
        last = wordarr[len(wordarr)-1]
        

        if last!='':
            preck[i]=last
            # print(preck[i],i)
            # print(preck)
            if len(tri.values(last))==0:
                f=0
            else:
                f=1
        cnt+=f
    # print("Ok print ; ",preck)
    return cnt,preck



def decryptPart(pos,e,key):
    msg2 = ['', '', '', '', '', '', '', '', '', '']
    for i in range(pos, e):
        pre = 0
        for j in range(0, 10):
            if i == 0:
                pre = 0
            else:
                pre = ara[j][i - 1]

            msg2[j] += chr(ara[j][i] ^ ((pre + key[i-pos]) % 256))

    # print(msg2)

    val,preck = checkDict(msg2)

    # print(val)
    # print(preck)
    # print(val,key)
    return val,preck,msg2

#combination part.......................





def combin(pos,s,e,allpos,strr):
    if s==e :
        val,preck,msg2 = decryptPart(pos,e,strr)
        global maxx
        global fkey
        global prepart2
        global finall

        if val>maxx:
            maxx = val
            fkey = strr.copy()
            prepart2 = preck
            finall = msg2
        return

    for i in range(0,len(allpos[s])):
        strr[s-pos] = allpos[s][i]
        combin(pos,s+1,e,allpos,strr) 

nulll = [0]*20
strr = [0] * 20
maxx = -1
fkey = [0] * 20
prepart =['', '', '', '', '', '', '', '', '', '']
prepart2 = prepart
finall = ['', '', '', '', '', '', '', '', '', '']

rslt2 = []

answ = ['', '', '', '', '', '', '', '', '', '']

for i in range (0,60,6):
    combin(i,i,i+6,allpos,strr)
    print(maxx)
    prepart = prepart2

    for j in range(0,6):
        rslt2+=[fkey[j]]
    for j in range(0,10):
        answ[j]+=finall[j]

    maxx = -1;
    

    strr = nulll.copy()
    fkey = nulll.copy()



# decode(rslt2)
# for i in msg:
#     print(i)



print("\nFinal decrypted message..........\n")
for i in answ:
    print(i)
print("\n-----------------------------------------\n")

print("OTP is : ")
for i in rslt2:
    print(chr(i),end='')
print("")
print("------------------------------------------------------")