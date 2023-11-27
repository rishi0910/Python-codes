l=list(map(int,input().split()))
l1=[]
for i in l:
    sq=i**2
    if(sq%2!=0):
        l1.append(sq)
print(l1)
