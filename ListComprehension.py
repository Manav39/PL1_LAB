temp = [1,2,3,4,5]

print("Square")
l = [ i**2 for i in temp]
print(l)

print("Range with even numbers")
l=[i for i in range(11) if i % 2 == 0]
print(l)

print("Range with odd numbers")
l=[i for i in range(11) if i%2!=0]
print(l)

print("Matrix using list")
l=[[j for j in range(3)] for i in range(3)]
print(l)

print("Vowels in string")
s="HelloWorld"
l = [i for i in s if i == 'a' or  i=='e'or i=='i'or i =='o'or i=='u']
print(set(l))

l=[[10,20,30],
   [40,50,60],
   [70,80,90]]

t = [[i[j] for i in l] for j in range(len(l[0]))]
print(t)