import sys

msg = input("Enter the message : ")
msgArr = []
for i in range(0,len(msg)):
    msgArr+=[ord(msg[i])]

key = input("Enter the key : ")
keyArr = []
for i in range(0,len(key)):
    keyArr+=[ord(key[i])]

if(len(msg)!=len(key)):
    print("Message and Key length aren't same :(")
    sys.exit()

encry = []
def encrypt(msg,key,encry):
    pre = 0
    for i in range(0,len(msg)):
        if i!=0:
            pre = encry[i-1]
        encry+=[msg[i]^((key[i]+pre)%256)]
    print("Encrypted cipher: ")
    print(encry)

decry = []
def decrypt(encry,key,decry):
    pre = 0
    for i in range(0, len(encry)):
        if i != 0:
            pre = encry[i - 1]
        decry += [encry[i] ^ ((key[i] + pre) % 256)]
    print("Decrypted Message: ")
    print(decry)
    mm = ''
    for i in range(0,len(decry)):
        mm+=chr(decry[i])
    print(mm)
print("")
encrypt(msgArr,keyArr,encry)
decrypt(encry,keyArr,decry)
