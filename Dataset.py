import pandas as pd

data = pd.Series([["USA",100,20],["India",120,30],["China",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200],["xpz",100,200]])

df = pd.DataFrame(data)
print(df.head())
print(df.describe())
print(df.tail())
print(df.min())
print(df.max())
print(df.info())
df.to_csv("temp.csv",index=False)

cols = ["Country","Price","Age"]
data = pd.read_csv("temp.csv",names=cols)
df = pd.DataFrame(data)
print(df.head())
arr = df.to_numpy()
print(arr)