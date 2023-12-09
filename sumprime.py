def prime(n):
   
    for i in range(2,n):
        if n%i==0:
            
            return False
    return True
x=int(input())
y=int(input())
s=0
for t in range(x,y+1):
    if (prime(t)):
        s+=t 
print(s)
    
            
