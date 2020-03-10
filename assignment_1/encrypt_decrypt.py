f = open("input2.txt", "r")
file = f.read()
#file = "Hello Bro Check it. If it works, then we will try to go for nexe problem that is decrypt the cipher text with out the key"
k = open("key.txt","r")
key= k.read()

#key = "FindTheKey"

inputFile = ""
outputFile = ""
originalFile = ""
for i in file:
    if (i >= 'a' and i <= 'z') or (i >= 'A' and i <= 'Z'):
        inputFile += i
length = len(key)


def val(x):
    if x >= 'a' and x <= 'z':
        return 97
    return 39


for i in range(len(inputFile)):
    tmp = (ord(inputFile[i]) - val(inputFile[i]) + ord(key[i % length]) - val(key[i % length])) % 52
    if (tmp > 25):
        outputFile += chr(tmp + 39)
    else:
        outputFile += chr(tmp + 97)
    if (i+1)%5==0:
        outputFile+=" "

o = open("output2.txt","w")
o.write(outputFile)

tmpfile = outputFile
outputFile = ""
for i in range(len(tmpfile)):
    if tmpfile[i]!=" ":
        outputFile+=tmpfile[i]

for i in range(len(outputFile)):
    tmp = (ord(outputFile[i]) - val(outputFile[i]) - ord(key[i % length]) + val(key[i % length]) + 52) % 52
    if (tmp > 25):
        originalFile += chr(tmp + 39)
    else:
        originalFile += chr(tmp + 97)

ori = open("original2.txt","w")

ori.write(originalFile.lower())

o.close()
ori.close()
k.close()
f.close()

print(inputFile)
print(tmpfile)
print(originalFile)
