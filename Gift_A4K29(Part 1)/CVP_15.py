n=int(input())
if n<2:
    print("Khong phai so nguyen to")
else:
    kt=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("Khong phai so nguyen to")
            kt=1
            break
    if kt==0:
        print("La so nguyen to")