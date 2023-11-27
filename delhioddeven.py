n=int(input("ENTER THE CARS"))
for i in range(0,n):
    y=int(input("ENTER THE CAR NUMBER"))
    odd=0
    even=0
    while y!=0:
        x=y%10
        even+=x
        odd+=x
        y=y//10
        if x%2==0 and even%4==0:
            print("Yes")
        elif x%2!=0 and odd%3==0:
            print("Yes")
            
            
           
else:
    print("No")
            
       
   
    
    
