import numpy as np

l = [1,2,3,4,5,6]
np_array = np.array(l)

print(l)
print(np_array)

print(l+l)
print(np_array+np_array)

#adding constant
np_array+=2
print(np_array)

np_ar = np.array([1,2,3,4])
for i in np_ar:
    print(type(i))
print(type(np_ar))

np_a = np.array([1,2,3,4,5])
print(np_a)
print(np_a[2:5])
np_a = np.arange(10)
print(np_a)
np_a = np.linspace(1,3,4)
print(np_a)
np_a = np.zeros(9,int)
print(np_a)
np_a = np.ones(5,int)
print(np_a)

og_a = np_a
print(og_a)
og_a[0]=5
print(np_a)

og_a = np_a.copy()
print(og_a)
og_a[2]=10
print(np_a)

og_a = np_a.view()
print(og_a)
og_a[2]=10
print(np_a)

l1 = np.array([1,2,3,4,5,6])
l2 = np.array([1,4,7,8,3,2])
print(l1+l2)
print(l1-l2)
print(l1*l2)
print(l1/l2)
print(l1**l2)
print(l1>l2)
print(l2>l1)
print(np.sin(l1))
l1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(l1.T)
l1=np.array([1,2,3,4,5,6,7])
print(l1.min())
print(l1.max())
print(l1.mean())
print(np.median(l1))

