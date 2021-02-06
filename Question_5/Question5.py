test=int(input())
for i in range (test):
    a,b=map(int,input().split())
    if a<=b:
        print(b-a)
    else:
        if a%b!=0:  
            print(b-(a%b))
        else:
            print(0)