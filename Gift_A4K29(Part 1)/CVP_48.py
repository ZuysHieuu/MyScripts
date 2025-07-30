import random
n=random.randint(1,100)
while True:
    m=int(input())
    if m>n:
        print("Lon hon")
    elif m<n:
        print("Nho hon")
    else:
        print("Dung roi")
        break