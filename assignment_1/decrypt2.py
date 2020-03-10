f = open("output2.txt","r")
tmp = f.read();
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
    if(count[i] >= maxx*5/7):
        keyarr[j]=i-now
        j+=1
        now = i

print(count)
print("max count match : "+ str(maxx))
print("initially Predicted key length: "+ str(keylen))

print("Predicted key length: ")
minn = 1e9
for i in range(0,j):
    print(str(keyarr[i]),end=", ")
    if minn> keyarr[i]:
        minn= keyarr[i]
print("")
print("Finally Predicted key length: "+ str(minn))
print("Key is : ")

frequency = [8.12,1.49,2.71,4.32,12.02,2.30,2.03,5.92,7.31,0.10,0.69,3.98,2.61,6.95,7.68,1.82,0.11,6.02,6.28,9.10,2.88,1.11,2.09,0.17,2.11,0.07]

relfreq = [0]*55

def val(k):
    if(k>='a' and k<='z'):
        return ord(k)-97
    return ord(k)-65
total = 0

answer1=""
answer2=""
answer3=""

for j in range(0,minn):
    for i in range(0,len(cipher)-j,minn):
        relfreq[val(cipher[i+j])]+=1
        total+=1
    for i in range(0,52):
        relfreq[i]=relfreq[i]*100/total
    maxrslt = 0.0
    maxrslt2 = 0.0
    maxrslt3 = 0.0
    rslt = -1
    rslt2 = -1
    rslt3 = -1

    for i in range(0,26):
        sum = 0.0
        for j in range(0,26):
            sum+=relfreq[(i+j)%26]*frequency[j]

        if sum>maxrslt:
            if maxrslt == -1:
                maxrslt2 =sum
                rslt2 = i
            else :
                maxrslt2 = maxrslt
                rslt2 = rslt
                maxrslt = sum
                rslt = i
        elif sum > maxrslt2:
            maxrslt2 = sum
            rslt2 = i

    # print(relfreq)
    # print(frequency)
    # print(chr(rslt+97))
    answer1+=chr(rslt + 97)
    answer2+=chr(rslt2+97)

print(answer1)
print(answer2)