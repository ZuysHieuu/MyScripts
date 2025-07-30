import numpy as np
a,b,c=map(float,input().split())
dt=b*b-4*a*c
print("C1: giai thong thuong")
if a==0 and b==0 and c==0:
    print("vo so nghiem")
if a==0 and b!=0:
    print(-c/b)
if dt<0:
    print("vo nghiem")
if dt>0:
    x1=(-b-dt**0.5)/(2*a)
    x2=(-b+dt**0.5)/(2*a)
    print(f"x1= {x1}, x2= {x2}")
if dt==0:
    print(-b/(2*a))
print("C2: giai = numpy")
print(np.roots([a,b,c]))
