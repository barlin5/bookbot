text = "HeLlo My Name Is dinguSsssss"
d = {}
for i in text:
    count = 0
    for char in text:
#        print(i)
        if char.lower() == i.lower():
            count +=1
#    print(count)
    print(d)
    d[i.lower()] = count
print(d)

