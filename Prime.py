n = int(input("Enter the number for which you want to find number "))
c = 0
for i in range(1,n+1):
    if n % i == 0:
        c = c + 1
if c == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")