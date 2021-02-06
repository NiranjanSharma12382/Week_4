def sum_digits2(n):
    sum=0
    for i in  str(n):
        sum+=int(i)
    return sum    
n,k=map(int,input().split())
while len(str(n))!=1:
    n=sum_digits2(n)
print (sum_digits2(k*n))