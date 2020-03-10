import re

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
        sett = {}
        sett =set(tst)
        allpos += [sett]


keyfind(rslt, allpos)

rony = 1
rar = []
for i in allpos:
    print(i)
    rar+=[len(i)]
    rony*=len(i)
print(rar)
print(rony)


msg = ['', '', '', '', '', '', '', '', '', '']


def decode(key):
    for i in range(0, 60):
        pre = 0
        for j in range(0, 10):
            if i == 0:
                pre = 0
            else:
                pre = ara[j][i - 1]

            msg[j] += chr(ara[j][i] ^ ((pre + key[i]) % 256))


decode(rslt)

print("\nInitial assumed message..........\n")
for i in msg:
    print(i)

# def decode5(pos, k):
#     msg5 = ['', '', '', '', '', '', '', '', '', '']
#     pre = 0
#     for i in range(pos, pos + 5):
#         for j in range(0, 10):
#             if (i == 0):
#                 pre = 0
#             else:
#                 pre = ara[j][i - 1];
#             ssss = k[i - pos];
#             msg5[j] += chr(ara[j][i] ^ ((pre + k[i - pos]) % 256));
#     return msg5;
#
#
# print(msg)
# print('--------------------------------------------------------------')
#
# #	Make dict set;
# wordsList = []
# f.close()
# f = open('dict.txt', 'r');
# while (True):
#     l = f.readline()
#     if (len(l) == 0):
#         break
#     wordsList += [l[0:len(l) - 1].lower()];
# words = set(wordsList);
# # create empty trie
# trie = StringTrie()
# # traverse through list of strings
# # to insert it in trie. Here value of
# # key is itself key because at last
# # we need to return
# for key in words:
#     trie[key] = key
#
#
# def prefixSearch(trie, prefix):
#     # values(search) method returns list
#     # of values of keys which contains
#     # search pattern as prefix
#     return trie.values(prefix)
#
#
# # Combination genation and decoding
# pre = ['', '', '', '', '', '', '', '', '', '']
# nmsgs = ['', '', '', '', '', '', '', '', '', '']
# pp = ['', '', '', '', '', '', '', '', '', '']
# # print(words)
# print(len(words))
# print('a' in words)
# mxf = 0;
# mnf = 100000;
# for i in range(0, 60, 5):
#
#     bk = 0;
#     flgMax = -1;
#     for i1 in range(0, len(rrre[i])):
#         for i2 in range(0, len(rrre[i + 1])):
#             for i3 in range(0, len(rrre[i + 2])):
#                 for i4 in range(0, len(rrre[i + 3])):
#                     for i5 in range(0, len(rrre[i + 4])):
#                         pcopy = pre.copy();
#                         k = [rrre[i][i1], rrre[i + 1][i2], rrre[i + 2][i3], rrre[i + 3][i4],
#                              rrre[i + 4][i5]]  # Prev should not changed
#                         m5 = decode5(i, k);
#                         # if(i==0):
#                         # 	print(m5)
#                         for j in range(0, 10):
#                             pcopy[j] += m5[j];
#
#                         prespls = [[]] * 10;
#                         flg = 0;
#                         araaa = [0] * 12
#                         for j in range(0, 10):
#                             prespls[j] = re.split(r'[.,?\-()\s!]', pcopy[j])
#                             # if(i==0):
#                             # 	print(prespls)
#                             f = 0;
#                             cccc = 0;
#                             for jj in range(0, len(prespls[j])):
#                                 if (prespls[j][jj] == ''):
#                                     continue;
#                                 if (jj != len(prespls[j]) - 1):
#                                     # print(prespls)
#                                     a = prespls[j][jj].lower();
#                                     # print(a)
#                                     if (a not in words):
#                                         f += 1;
#                                         # print('asi')
#                                         araaa[j] = 1
#                                     else:
#                                         cccc += 1;
#                                 #  	print(a)
#                                 else:
#                                     if (len(prefixSearch(trie, prespls[j][jj])) == 0):
#                                         f += 1
#                                         araaa[j] = 2
#                                     else:
#                                         cccc += 1
#                                         if (m5[4] == ' ' or m5[4] == '.' or m5[4] == ',' or m5[4] == '-' or m5[
#                                             4] == '?' or m5[4] == '(' or m5[4] == ')' or m5[4] == '!'):
#                                             pcopy[j] = prespls[j][jj] + ' ';
#                                         else:
#                                             pcopy[j] = prespls[j][jj];
#
#                             if (f == 0 or cccc > 100):
#                                 flg += 1;
#                             # p[j]+=
#                             mnf = min(mnf, f);
#                         # if(flg>flgMax):
#                         # 	pre=pcopy.copy();
#                         # flgMax=max(flgMax,flg);
#                         if (i > 50):
#                             print(flg);
#                         if (flg > 6):  # --------------------------------->
#                             print(araaa)
#                             print(prespls)
#                             print(i)
#                             print(flg)
#                             print(k)
#                             for j in range(0, 10):
#                                 nmsgs[j] += m5[j];
#                             bk = 1;
#                             pre = pcopy.copy();
#
#                         mxf = max(mxf, flg)
#                         if (bk == 1):
#                             break
#                     if (bk == 1):
#                         break
#                 if (bk == 1):
#                     break
#             if (bk == 1):
#                 break;
#         if (bk == 1):
#             break
# print(mxf, mnf)
# print(nmsgs);


