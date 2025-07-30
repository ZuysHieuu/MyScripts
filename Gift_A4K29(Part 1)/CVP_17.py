n=int(input())
d=0
while n>0:
    d=d*10+n%10
    n//=10
print(d)