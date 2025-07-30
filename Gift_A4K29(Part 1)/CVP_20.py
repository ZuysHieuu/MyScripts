n=int(input())
a=[]
a.append(0)
a.append(1)
for i in range(n):
    if i<=1:
        print(i,end=" ")
    else:
        a.append(a[i-1]+a[i-2])
        print(a[i],end=" ")