def dt(s):
    if not s or not s.strip():
        return 0
    return s.strip().split()
def dn(s):
    return s[::-1]
def dx(s):
    return s==dn(s)
def ch(s):
    if not s:
        return ""
    return " ".join(x.capitalize() for x in s.strip().split())
s=str(input())
print(ch(s))
