n = int(input("Enter the number : "))

for i in range(0 , n):
    for j in range(0,i+1):
        print("*",end=" ")
    for j in range(n , i , -1):
        print(" ",end=" ")
    for j in range (n,i,-1):
        print(" " , end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
