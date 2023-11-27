n=input()
c = "aeiou"
count = 0
for i in n:
    if i in c:
        count = count + 1
        
print(count)
