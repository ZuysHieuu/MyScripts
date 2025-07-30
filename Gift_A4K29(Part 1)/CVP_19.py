n=int(input())
d=0
for i in range(1,int(n**0.5)+1):
    if n%i==0:
        d+=i
        if i!=n//i:
            d+=n//i
if d==2*n:
    print("La so hoan hao")
else:
    print("Khong phai so hoan hao")