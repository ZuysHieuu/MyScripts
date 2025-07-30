a,b=map(int,input().split())
c,d=a,b
while a!=b:
    if a>b:
        a-=b
    if b>a:
        b-=a
print(f"UCLN: {a}, BCNN: {c*d//a}")