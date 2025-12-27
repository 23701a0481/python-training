x=list(map(int,input().split()))
min1=max1=x[0]
for i in range(1,len(x)):
    if x[i]<min1:
        min1=x[i]
    if x[i]>max1:
        max1=x[i]
print(min1,max1)
OUTPUT:
2 5 7 1 9 
1 9
