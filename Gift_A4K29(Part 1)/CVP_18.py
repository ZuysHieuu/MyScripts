a,b=map(int,input().split())
while a!=b:
    if a>b:
        a-=b
    if b>a:
        b-=a
print(a)