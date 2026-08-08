a=[1,2,3,4,5,6,7]
for i in range(1,7):
    print(i)
    a.append(2)
    a.remove(2)
    a.insert(1,9)
    print(a[1],end=" ")
    print(a[3],end=" ")
    res=a[1:4]
    print(res)
    print(a)