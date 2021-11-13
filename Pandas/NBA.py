import pandas as pd
import numpy as np
df = pd.read_csv("nba.csv")
soru1 = df.head(10)
soru2 = len(df.index)
"""def soru3(df):
    total = df.sum().sum()
    piece = df.size - df.isnull().sum().sum()
    return total // piece
    """
soru3 = df.Salary.mean()
soru4 = df.Salary.max()
soru5 = df[df.Salary == df.Salary.max()]["Name"]
soru6 = df[(df.Age>20)&(df.Age<25)].sort_values("Age",ascending=False)[["Name","Team"]]
newdf = df.fillna("noinput")
soru7 = newdf[newdf.Name.str.contains("Holland")].Team
soru8 = df.groupby("Team").Salary.mean()
soru9 = len(df.groupby("Team"))
soru10 = df.groupby("Team").count()["Name"]
soru11 = df.Name.str.find("and")

print(df.columns)
print(df)
print("<<<<<<<<<<**********>>>>>>>>>>")
print(soru11)


