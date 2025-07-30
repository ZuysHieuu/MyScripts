n=int(input())
m,k=n,0
while m>0:
    k=k*10+m%10
    m//=10
if k==n:
    print("Doi xung")
else:
    print("Khong doi xung")