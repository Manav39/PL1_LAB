from functools import reduce

#Lambda

str1="Geeksforgeeks"
upper = lambda str1 : str1.upper()
print(upper(str1))

square = lambda x : x*x
print(square(4))

Max = lambda a,b:a if(a>b) else b
print(Max(4,5))



def addition(a):
    return a+a

num=(1,2,3,4)
result = list(map(addition,num))
print(result)

def sqaure(a):
    return a*a
res = list(map(square,num))
print(res)

res = list(map(lambda x:x*x,num))
print(res)

res = list(map(lambda x,y:x+y,num,result))
print(res)

num=[1,2,3,4,5,6,7,8,9,10]
res = list(map(lambda x:x if x%2==0 else x**2,num))
print(num)


res = list(filter(lambda x : x%2==0,num))
print(res)

num="manava"
def fun(variable):
    letters=['a','e','i','o','u']
    if variable in letters:
        return True
    else:
        return False

res = list(filter(fun,num))
print(res)


num=[1,3,5,6,2]
print(reduce(lambda a,b:a+b,num))
print(reduce(lambda a,b:a if a>b else b,num))
