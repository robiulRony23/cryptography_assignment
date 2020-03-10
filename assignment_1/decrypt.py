f=open('output1.txt','r');
C=f.read();
temp='';
for x in C:
	if (x>='a' and x<='z') or (x>='A' and x<='Z'):
		temp+=x;
C=temp;
l=len(C);
matches=[]
maxCnt=0;
for i in range(1,int((4*l)/5)):
	cnt=0;
	for j in range(0,l-i):
		if(C[j]==C[i+j]):
			cnt+=1;
	matches+=[cnt];
	maxCnt=cnt if (maxCnt<cnt) else maxCnt;

releventDistances=[];
print('maximum match:'+ str(maxCnt));
def needed(a,m):
	if (a>=2 and a>=m*6/7):
		return bool(1);
	else:
		return bool(0);
disLen=len(matches);
last=-1;

for i in range(0,disLen):
	if (last==-1 and needed(matches[i],maxCnt)):
		last=i;
	else:
		if last != -1 and needed(matches[i],maxCnt):
			x=i-last
			last=i
			releventDistances+=[x];
print('Matches are:')
print(matches);
print('Probable key lengths are:')
print(releventDistances);

mn=1000000;
for i in range(0,len(releventDistances)):
	mn=min(mn,releventDistances[i]);

print('LEN:'+str(mn));

def letKey(kl,l,C):
	S='';
	fre=[0.0812,0.0149,0.0271,0.0432,0.1202,0.0230,0.0203,0.0592,0.0731,0.0010,0.0069,0.0398,0.0261,0.0695,0.0768,0.0182,0.0011,0.0602,0.0628,0.0910,0.0288,0.0111,0.0209,0.0017,0.0211,0.0007]
	key='';
	for i in range(0,kl):
		aral=[0];
		arau=[0]
		for j in range(0,26):
			aral+=[0];
			arau+=[0];
		cnt=0;
		for j in range(i,l,kl):
			cnt+=1;
			if(C[j]>='a' and C[j]<='z'):
				aral[ord(C[j])-97]+=1;
			else:
				arau[ord(C[j])-65]+=1;
		raral=[];
		rarau=[];
		for j in range(0,26):
			raral+=[aral[j]/cnt];
		for j in range(0,26):
			rarau+=[arau[j]/cnt];

		print(raral);
		mxval=-1.0;
		mxi=-1;
		for j in range(0,26):
			sum=0;
			for k in range(0,26):
				sum+=fre[k]*raral[(k+j)%26];
			if (mxval<sum):
				mxval=sum;
				mxi=j;
		key+=chr(ord('a')+mxi);
	return key;
key=letKey(mn,l,C);
print(key);
# Build frequency array
