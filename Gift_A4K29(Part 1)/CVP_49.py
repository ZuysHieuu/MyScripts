a=float(input())
b=float(input())
c=str(input())
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    if b!=0:
        print(a/b)
    else:
        print("Loi!")
else:
    print("None")