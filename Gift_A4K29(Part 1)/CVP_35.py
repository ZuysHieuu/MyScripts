n=int(input())
a=[]
for i in range(n+10):
    a.append(1)
for i in range(2,n+1):
    if a[i]==1:
        print(i,end=" ")
        for j in range(i*i,n+1,i):
            a[j]=0