a,b,c=map(float,input().split())
if a==b==c:
    print("Tam giac deu")
elif a==b or b==c or c==a:
    print("Tam giac can")
elif a**2+b**2==c**2 or b**2+c**2==a**2 or c**2+a**2==b**2:
    print("Tam giac vuong")
else:
    print("Tam giac thuong")