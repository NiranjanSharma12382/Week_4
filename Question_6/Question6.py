n=int(input())
collection_at_edge=6*(4**(n-3))
collection_in_middle=9*(n-3)*(4**(n-4))
if n>=4:
    print(4*(collection_at_edge+collection_in_middle))
elif n==3:
    print(4*(collection_at_edge))
else:
    print(n)