
def isValid(a):
    if len(a)>8:
        return False
    for i in range(0,len(a)):
        if (a[i]!='0' and a[i]!='1'):
            return False
    return True

a=input("Enter First bit String (8 length): ")
if isValid(a)==False:
    print("Invalid input.:(")
    exit()

b=input("Enter Second bit String (8 length): ")
if isValid(b)==False:
    print("Invalid input.:(")
    exit()
a= a.zfill(8)
b= b.zfill(8)

op=input("Enter the operator(+,-,*,/): ")
if op not in {'+','-','*','/'}:
    print("Invalid input.:(")
    exit()
elif op=='/' and int(b,2)==0:
    print("Can not divide by zero\nInvalid input.:(")
    exit()

def leftOnePos(a):
    for i in range(0,8):
        if a[i]=='1':
            return 7-i
    return -1

def addSub(a,b):
    aa = int(a,2)
    bb = int(b,2)

    return aa^bb

def multiply(aa,bb,mm):

    rem = 0
    while (bb != 0):
        if (bb & 1 != 0):
            rem = rem ^ aa
        tmp = aa & 0x80
        aa = aa << 1
        if tmp != 0:
            aa = aa ^ mm
        bb = bb >> 1
    return rem

def division(a,b):
    aa = leftOnePos(a)
    bb = leftOnePos(b)

    div = 0

    valA=int(a,2)
    valB=int(b,2)

    while aa>=bb:

        tmp= aa-bb
        div+=(1<<tmp)
        valA=(valB<<tmp)^valA
        aa=leftOnePos(bin(valA).lstrip('0b').zfill(8))
    return div,valA



ans = -1
m= '100011011'
arrGF={}

def gf(m):
    global arrGF
    for i in range(1,256):
        for j in range(1,256):
            if multiply(i,j,m)==1:
                arrGF[i]=j
                break

def inv(bb,mm):
    for i in range(0,256):
        if multiply(bb,i,mm)==1:
            return i

def gfDivision(aa,bb,mm):
    global arrGF
    # tmp =arrGF[bb]
    tmp = inv(bb,mm)

    div = multiply(aa,tmp,mm)

    return div

aa = int(a, 2)
bb = int(b, 2)
mm = int(m,2)



if (op=='+' or op=='-'):
    ans = addSub(a,b)
    if op=='+':
        print("\nAddition of "+a+" and "+b +" is : ",end='')
    else:
        print("\nSubtraction of " + a + " and " + b + " is : ", end='')
    print(bin(ans).lstrip('0b').zfill(8))
elif op=='*':
    ans = multiply(aa,bb,mm)
    print("\nMultiplication of " + a + " and " + b + " is : ", end='')
    print(bin(ans).lstrip('0b').zfill(8))
elif op=='/':
    # ans,rem = division(a,b)
    gf(mm)
    ans= gfDivision(aa,bb,mm)
    print(aa,bb,mm,ans)
    print("\nDivision of " + a + " and " + b + " is : "+str(bin(ans).lstrip('0b').zfill(8)))
    # print("Quotient is : ",end='')
    # print(bin(ans).lstrip('0b').zfill(8))
    # print("Remainder is : ", end='')
    # print(bin(rem).lstrip('0b').zfill(8))




