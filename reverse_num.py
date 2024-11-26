
def rev(num):
    sum=0
    while num!=0:
        rem=num%10
        sum=rem+sum*10
        num=num//10
    print(sum)
num=int(input("enter num="))
rev(num)
