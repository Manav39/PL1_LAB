l = []
print("Enter the number of elements you want to enter in list")
n = int(input())
for i in range(0,n):
    x = int(input("Enter the element"))
    l.append(x)
summ = 0
def sumele(l,i):
    global summ
    if i == n:
        return
    summ = summ + l[i]
    sumele(l,i+1)

sumele(l,0)
print(summ)
