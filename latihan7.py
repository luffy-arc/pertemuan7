a = 100000000
for x in range (1,9):
    if (x>=1 and x<=2):
        b = a*1
        print("laba bulan ke -",x," :",b)
    if (x>=3 and x<=4):
        c = a*0.2
        print("laba bulan ke -",x," :",c)
    if (x>=5 and x<=7):
        d = a*0.4
        print("laba bulan ke -",x," :",d)
    if (x==8):
        e = a*0.3
        print("laba bulan ke -",x," :",e)
z = b+b+c+c+d+d+d+e
print("total laba adalah :", z)