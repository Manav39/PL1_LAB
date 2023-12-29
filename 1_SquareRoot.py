
n = int(input("Enter the number for finding square root"))
if n == 1:
    print(f"square root of {n} is 1")
else:
    res = False
    for i in range(1,n//2):
        if i * i == n:
            res = True
            print(f"Square Root is {i}")
            break



