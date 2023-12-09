d={}
k=int(input())
st=input()
r=('')

for i in st:
    if i in d:
        d[i]=d[i]+1
    else:
        d[i]=1

for i in st:
    if d[i]<k:
       r=r+i
print(r)       

    
    
    
