def pal(num):
    sum=0
    temp=num
    while num!=0:
        rem=num%10
        sum=rem+sum*10
        num=num//10
    if temp==sum:
        print("palindrome")
    else:
        print("not palindrome")
num=int(input("enter num="))
pal(num)
