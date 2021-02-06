def power(a,b):
    if b==0:
        return 1
    if b==1:
        return a
    temp=power(a,int(b/2))
    result=temp*temp
    if b%2==1:
        result*=a
    return result                       

x,y=map(int,input().split())
print((power(x,y))%(10**9+7))

