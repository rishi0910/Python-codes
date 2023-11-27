n=int(input("Enter number here: "))
sum=0
count=0
#numerator loop
for i in range (0,n+1):
    count=0
    #denomitor loop
    for j in range(1,n+1):
        if i%j==0:
            count=count+1
    if count==2:
        sum=sum+i
print(sum)


