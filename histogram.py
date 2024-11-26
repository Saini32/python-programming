def histo(item):
    for n in item:
        output=" "
        item=n
        while item>0:
            output+="*"
            item=item-1
        print(output)
histo([2,3,6])
