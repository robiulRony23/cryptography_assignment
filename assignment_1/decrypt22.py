f = open("output2.txt","r")
tmp = f.read();
o = open("original2.txt","r")
original = o.read()

cipher = ""
for i in range(len(tmp)):
    if(tmp[i]!=" "):
        cipher+=tmp[i]
count = [0]*len(cipher)

maxx = -1
keylen = -1
keyarr = [0]*int(len(cipher)/3)
cipher.lower()
for i in range(1,int(len(cipher)/3)):
    for j in range(0,len(cipher)-i):
        if cipher[j]==cipher[i+j] :
            count[i]+=1;
    if count[i]>maxx:
        maxx= count[i]
        keylen = i
now = 0
j=0
for i in range(1,int(len(cipher)/3)):
    if(count[i] >= maxx*3/4):
        keyarr[j]=i-now
        j+=1
        now = i

print(count)
print("max count match : "+ str(maxx))


print("Predicted key length: ")

keycount= [0]*1000
for i in range(0,j):
    print(str(keyarr[i]),end=", ")
    keycount[keyarr[i]]+=1

firstkeylen = -1
secondkeylen = -1
firstkey = -1
secondkey = -1

for i in range(1,len(keycount)):
    if(keycount[i]>firstkey):
        secondkey = firstkey
        secondkeylen = firstkeylen
        firstkey = keycount[i]
        firstkeylen = i
    elif (keycount[i]>secondkey):
        secondkey = keycount[i]
        secondkeylen = i


print("")

def ckeckMatch(file):
    cnt = 0;
    mismatch = 0;

    for i in range(len(file)):
        if(file[i]!=original[i]):
            mismatch+=1
        cnt+=1

    print("Total character : "+str(cnt))
    print("Mismatched : "+ str(mismatch))
    chk = (cnt-mismatch)*100/cnt
    print("Matching percentage : "+str(chk)+"%")

def vall(x):
    if x >= 'a' and x <= 'z':
        return 97
    return 65
def decrypt(key,length):
    outputFile = cipher

    print("key is : "+key)

    originalFile =""
    for i in range(len(outputFile)):
        tmp = (ord(outputFile[i]) - vall(outputFile[i]) - ord(key[i % length]) + vall(key[i % length]) + 26) % 26
        if (tmp > 25):
            originalFile += chr(tmp + 39)
        else:
            originalFile += chr(tmp + 97)
    print("Text is:")
    print(originalFile)
    ckeckMatch(originalFile)

def keyfind(keyLenPredit):
    frequency = [0.0812, 0.0149, 0.0271, 0.0432, 0.1202, 0.0230, 0.0203, 0.0592, 0.0731, 0.0010, 0.0069, 0.0398, 0.0261,
                 0.0695, 0.0768, 0.0182, 0.0011, 0.0602, 0.0628, 0.0910, 0.0288, 0.0111, 0.0209, 0.0017, 0.0211, 0.0007]
    relfreq = [0] * 55

    def val(k):
        if (k >= 'a' and k <= 'z'):
            return ord(k) - 97
        return ord(k) - 65

    total = 0

    answer1 = ""
    answer2 = ""

    for j in range(0, keyLenPredit):
        for i in range(0, len(cipher) - j, keyLenPredit):
            relfreq[val(cipher[i + j])] += 1
            total += 1
        for i in range(0, 52):
            relfreq[i] = relfreq[i] / total
        maxrslt = 0.0
        maxrslt2 = 0.0

        rslt = -1
        rslt2 = -1

        for i in range(0, 26):
            sum = 0.0
            for j in range(0, 26):
                sum += relfreq[(i + j) % 26] * frequency[j]

            if sum > maxrslt:
                if maxrslt == -1:
                    maxrslt2 = sum
                    rslt2 = i
                else:
                    maxrslt2 = maxrslt
                    rslt2 = rslt
                    maxrslt = sum
                    rslt = i
            elif sum > maxrslt2:
                maxrslt2 = sum
                rslt2 = i

        answer1 += chr(rslt + 97)
        answer2 += chr(rslt2 + 97)

    decrypt(answer1,keyLenPredit)

    decrypt(answer2, keyLenPredit)

print("Approximately Predicted key length(1st): "+ str(firstkeylen))
keyfind(firstkeylen)
print("")
print("Approximately Predicted key length(2nd): "+ str(secondkeylen))
keyfind(secondkeylen)




