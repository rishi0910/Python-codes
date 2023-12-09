x=int(input())
st=str(x)
r=("")
import math
maxi=-math.inf
mini=math.inf
for i in st:
    t=int(i)
    if t>maxi:
        maxi=t
    if t<mini:
        mini=t
for i in st:
    if i==str(maxi) or i==str(mini):
        continue
    else:
        r=r+i

print(int(r))
