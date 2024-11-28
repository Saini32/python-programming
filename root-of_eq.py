import math
a=int(input("enter a="))
b=int(input("enter b="))
c=int(input("enter c="))
t=b*b-4*a*c
t1=math.sqrt(t)
r=(-b+(t1))/2*a
r1=(-b-(t1))/2*a
print(r)
print(r1)
