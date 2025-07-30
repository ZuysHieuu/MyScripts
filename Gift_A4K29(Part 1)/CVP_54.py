import random
sap,ngua=0,0
for i in range(1000):
    x=random.randint(0,1)
    if x==0:
        ngua+=1
    else:
        sap+=1
print(f"Sap: {sap} lan ({sap/10:.1f}%), Ngua: {ngua} lan ({ngua/10:.1f}%)")