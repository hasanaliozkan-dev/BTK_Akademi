import pandas as pd

data = pd.read_csv("./ReviewContent.csv")
print(data)
print("<<<<<<<<<<**********>>>>>>>>>>")
"""
print(data.info())
print(data.memory_usage())
print(data["Room Price"].sum())
print(data["City"].value_counts())
print(data["City"].sort_values())
print(data["Room Type"].value_counts())
print(data["Room Price"].sort_values(ascending=False))
print(data["City"].sort_values()[100:120])

print(data.sort_values("Room Price",ascending=False)["Review Content"])
print(data[data["Room Price"] > 700]["Review Content"])
mask = data["City"] == "London"
print(data[mask])

mask = data["Room Type"] == "Private room"

print(data[mask]["Room Price"].max())
mask = (data["Room Price"] >= 60) & (data["Room Price"] <= 100)
print(data[mask].sort_values("Room Price"))
#isin
mask = data["City"].isin(["London","Amsterdam","Paris","Madrid"])
print(data[mask])
#between
mask = data["Room Price"].between(60,100)
print(data[mask])
mask = data["Review Date"].between("2013-01-01","2014-01-01")
print(data[mask])
#duplicated
data.sort_values("City",inplace=True)
print(data["City"])
mask = ~data["City"].duplicated()
print(data[mask]["City"])
#drop_duplicates
print(len(data.drop_duplicates(subset=["City"])))"""
