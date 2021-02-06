test=int(input())
def tribonocci(a):
    if a<=2:
        return 0
    elif a>2 and a<4:
        return 1    
    else:
        b=tribonocci(a-1)+tribonocci(a-2)+tribonocci(a-3)
        return b
for i in range(test):
    n=int(input())
    print(tribonocci(n))

