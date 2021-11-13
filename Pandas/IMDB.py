import pandas as pd
#soru1
df = pd.read_csv('IMDB.csv')
soru2 = df.head()
soru3 = df.head(10)
soru4 = df.tail()
soru5 = df.tail(10)
soru6 = df["Movie_Title"]
soru7 = df["Movie_Title"].head()
soru8 = df[["Movie_Title","Rating"]].head()
soru9 = df[["Movie_Title","Rating"]].tail(7)
soru10 = df[5:][["Movie_Title","Rating"]].head()
soru11 = df[df["Rating"] > 8][["Movie_Title","Rating"]].head(50)
soru12 = df[(df['YR_Released']>=2014) & (df['YR_Released']<=2015)]["Movie_Title"]
soru13 = df[(df["Rating"]>=8) &(df["Rating"]<=9)|(df["Num_Reviews"]>100.000)][["Num_Reviews","Rating"]]
print(df)
print("<<<<<<<<<<<<<<<<<<<<********************>>>>>>>>>>>>>>>>>>>>")
print(soru13)

