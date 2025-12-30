def fib(n):
    a=1
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b 
        a=b
        b=c 
        print(c)
n=int(input())
fib(n)
OUTPUT:
5
1 1 2 3 5
