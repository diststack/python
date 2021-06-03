import pandas as pd


df = pd.read_csv('data2.csv')
new_df = df.dropna()
print(new_df.to_string())

x = df["Calories"].mean()

print(df["Calories"].fillna(x).to_string())


# cleaning wrong format

df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].to_string())


for x in df.index:
    if df.loc[x, "Duration"] > 120:
        print(df.loc[x, "Duration"])
        df.loc[x, "Duration"] = 120
        print(df.loc[x, "Duration"])

print(df.duplicated())
