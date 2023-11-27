l=[10,20,30]
n=len(l)
temp=l[n-1]
i=n-2
while i>=0:
    l[i+1]=l[i]
    i=i-1
l[0]=temp
print(l)
