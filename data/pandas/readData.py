import pandas as pd

df = pd.read_csv('data.csv')

print(df.head(4))
print(df.tail(5))
print(df.info())
print("\nreading json  ")
df = pd.read_json('data.json')
print(df)
