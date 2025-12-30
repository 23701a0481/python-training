def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
arr=list(map(int,input().split(",")))
target=int(input())
print(linear_search(arr,target))
OUTPUT:
arr=2,5,4,3,7,9
target=9
5
