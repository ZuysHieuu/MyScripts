n=int(input())
score=0
a=list(map(float,input().split()))
for i in a:
    score+=i
score/=n
if score>=9.0:
    print(" Xuat sac")
elif score>=8.0:
    print("Gioi")
elif score>=6.5:
    print("Kha")
elif score>=5.0:
    print("Trung binh")
else:
    print("Yeu")