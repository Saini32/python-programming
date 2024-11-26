sum=0
for i in range(5):
    sum=sum+i
print(sum)

v=int(input("enter num="))
a=0
b=1
for n in range(0,v):
    if n<=1:
        c=n
    else:
        c=a+b
        a=b
        b=c
    print(c)
