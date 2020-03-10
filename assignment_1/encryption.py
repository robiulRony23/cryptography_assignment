f = open("input1.txt", "r")
file = f.read()
k = open("key.txt","r")
key= k.read()

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
    return 65


for i in range(len(inputFile)):
    tmp = (ord(inputFile[i])-val(inputFile[i]) + (ord(key[i % length]) - val(key[i % length])) % 26)%26
    if (val(inputFile[i]) == 97):
        outputFile += chr(tmp + 97)
    else:
        outputFile += chr(tmp + 65)
    if (i+1)%5==0:
        outputFile+=" "

o = open("output1.txt","w")
o.write(outputFile)
o.close()

tmpfile = outputFile
outputFile = ""
for i in range(len(tmpfile)):
    if tmpfile[i]!=" ":
        outputFile+=tmpfile[i]

for i in range(len(outputFile)):
    tmp = (ord(outputFile[i])-val(outputFile[i]) - (ord(key[i % length]) - val(key[i % length])) % 26 + 26)%26
    if (val(outputFile[i]) == 97):
        originalFile += chr(tmp + 97)
    else:
        originalFile += chr(tmp + 65)
ori = open("original.txt","w")
ori.write(originalFile)

ori.close()
k.close()
f.close()

print(inputFile)
print(tmpfile)
print(originalFile)
