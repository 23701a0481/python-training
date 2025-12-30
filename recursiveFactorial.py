def facti(n):
    if n==0 or n==1:
        return n
    return n*facti(n-1)
print(facti(6))
OUTPUT:
6*5*4*3*2*1
720
