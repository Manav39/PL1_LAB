n = int(input("Enter the number of elements you want to find in fibonaaci series "))
if n == 1:
    print(0)
else:
    a = 0
    b = 1
    print(0)
    print(1)
    for i in range(3,n+1):
        c = a+b
        print(c)
        a = b
        b = c

