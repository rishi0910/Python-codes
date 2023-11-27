a=int(input("no. of class held"))
b=int(input("no. of classes attended"))
c=(b/a)*100
d=input("Any medical issue")
if (c<=75):
  if(d=="Yes"):
    print(c,"Student Allowed")
  else:
    print(c,"student not allowed")
else:
  print("student allowed")
