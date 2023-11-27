
m = int(input("Enter lower limit : "))
sum = 0
for i in range (2, m+1):
    rishi = True
    for j in range(2 , i):
        if i%j == 0:
            rishi = False
            break
    if rishi == True:
        sum=sum+i
        print(i)
print(sum)

    

