def find(st,a):
    i=0
    while i<len(st):
        if st[i]==a:
            return i
        i=i+1
    return -1
print(find("sneha","e"))
