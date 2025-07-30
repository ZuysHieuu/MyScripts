import numpy as np
a,b,c,d,e,f=map(float,input().split())
print("C1: dinh thuc")
D=a*e-b*d
Dx=c*e-b*f
Dy=a*f-c*d
if D!=0:
    print(f"x= {Dx/D}, y= {Dy/D}")
elif Dx==Dy==0:
    print("Vo so nghiem")
else:
    print("Vo nghiem")
print("C2: dung Numpy")
try:
    A=np.array([[a,b],[d,e]])
    B=np.array([c,f])
    x,y=np.linalg.solve(A,B)
    print(f"x= {x}, y={y}")
except np.linalg.LinAlgError:
    print("Vo nghiem")