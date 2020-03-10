f = open("input.txt","r")
f1 = f.readline()
word1 = [int(i,16) for i in f1.split()]
print(word1)
f2 = f.readline()
word2 = [int(i,16) for i in f2.split()]
print(word2)
word =[0]*len(word1)
for i in range(len(word1)):
    word[i]=word1[i]^word2[i]
print(word)

f.close()
f = open("word.txt","r")
wordlist =[]
while(True):
    txt = f.readline()
    if(len(txt)==0):
        break
    elif(len(txt)==9):

        wordlist+=[txt[0:8]]
wordset = {}
wordset =set(wordlist)

for i in wordlist:
    xor=""
    for j in range(0,8):
        xor+=chr(word[j]^ord(i[j]))
    if xor in wordset:
        print(i)
        print(xor)
        break