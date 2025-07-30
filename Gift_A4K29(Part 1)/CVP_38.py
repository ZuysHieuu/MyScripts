n=int(input())
ma=-1e18
a=list(map(int,input().split()))
for i in a:
    ma=max(ma,i)
print(ma)