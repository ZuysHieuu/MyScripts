import math
def dt_hv(n):
    return n*n
def dt_hcn(a,b):
    return a*b
def dt_ht(r):
    return r*r*math.pi
def dt_htg(a,b,c):
    s=(a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**0.5
hinh=str(input())
if hinh=='hinh vuong'
    print(dt_hv)
if hinh=='hinh chu nhat'
    print(dt_hcn)
if hinh=='hinh tron'
    print(dt_ht)
if hinh=='hinh tam giac'
    print(dt_htg)
