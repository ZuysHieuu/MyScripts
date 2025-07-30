a,b=map(int,input().split())
if a in [1,3,5,7,8,10,12]:
    print(31)
elif a in [4,6,9,11]:
    print(30)
else:
    if (b%4==0 and b%100!=0) or b%400==0:
        print(29)
    else:
        print(28)