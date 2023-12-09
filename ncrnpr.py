def fact(n):
    ans=1
    for i in range(1,n+1):
        ans=ans*i
    return ans
n=int(input())
r=int(input())
print(fact(n)/(fact(r)*fact(n-r)))
print(fact(n)/fact(n-r))


