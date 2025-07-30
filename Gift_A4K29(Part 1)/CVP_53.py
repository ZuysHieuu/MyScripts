import numpy as np
x1,y1,x2,y2=map(float,input().split())
print("C1: thong thuong")
print(((x2-x1)**2+(y2-y1)**2)**0.5)
print("C2: dung numpy")
xy1=np.array([x1,y1])
xy2=mp.array([x2,y2])
print(np.linalg.norm(xy2-xy1))
