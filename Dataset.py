import pandas as pd
import matplotlib.pyplot as plt
data = pd.Series([["USA",100,20],["India",120,30],["China",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200]])

df = pd.DataFrame(data)
print(df.head())
print(df.describe())
print(df.tail())
print(df.min())
print(df.max())
print(df.info())
df.to_csv("temp.csv",index=False)

data = [["USA",100,20],["India",120,30],["China",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200]]
df = pd.DataFrame(data,columns=["country",'age',"price"])
print(df['country'])
print(df.head())
print(df.T)
print(df.drop_duplicates())
arr = df.to_numpy()
print(df.dtypes)
print(df.loc[1:2])
# print(arr)
plt.plot(df['age'],df['price'])


# %%
