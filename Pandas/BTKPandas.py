import pandas as pd
from numpy.random import randn
import numpy as np
"""SERIES"""
# numbers = [20,30,40,50]
# letters = ['a','b','c','d']
# numberSerie = pd.Series(numbers)
# letterSerie = pd.Series(letters)
# #we can write like this
# numbersAndLetters = pd.Series(numbers,letters)
# x = pd.Series(5,[1,2,3,4,5,])
# dict = {'a':10,'b':20,'c':30,'d':40}
# dictSerie = pd.Series(dict)
# print(x)
# print()
# print(numberSerie)
# print()
# print(letterSerie)
# print()
# print(numbersAndLetters)
# print(dictSerie)
# randomNumbers = np.random.randint(0,10,6)
# randomSeries = pd.Series(randomNumbers)
# print(randomSeries)
#PandasSeries = pd.Series([20,30,40,50],['a','b','c','d'])
#result = PandasSeries[0]
#result = PandasSeries[-1]
#result = PandasSeries[:2]
#result = PandasSeries[-2:]
#result = PandasSeries['a']
#result = PandasSeries[['a','c']]
# result = PandasSeries.ndim
# result = PandasSeries.dtype
# result = PandasSeries.shape
# result = PandasSeries.sum()
# result = PandasSeries.max()
# result = PandasSeries.mean()
# result = np.sqrt(PandasSeries)
# result = PandasSeries >35
"""DATA FRAMES"""
#df = pd.DataFrame()
# df = pd.DataFrame([1,2,3,4])
# print(df)
# s1 = pd.Series([1,2,3,4])
# s2 = pd.Series([5,6,7,8])
# data =dict(apples = s1,oranges = s2)
# df = pd.DataFrame(data)
# data = [["Ahmet",50],["Ali",60],["Büşra",900],["Mert",40]]
# df = pd.DataFrame(data,columns=["Name","Grade"],index=[1,2,3,4])
# print(df)
"""Reading Csv"""
#dfcsv = pd.read_csv('sample.csv')
#print(dfcsv)
"""Reading Json"""
#dfjson = pd.read _json('sample.json',encoding='UTF-8')
#print(dfjson)
"""Reading Excel"""
# dfexcel = pd.read_excel("sample.xlsx")
# print(dfexcel)

"""WORKİNG ROWS AND COLUMNS"""
#df = pd.DataFrame(randn(3,3),index=['A','B','C'],columns=["column1","column2","column3"])
#result = df["column1"]
#result = df[["column1","column2"]]
"""loc["row","column"] => loc["row"] ===> loc[":", "column"]"""
# result = df.loc["A"]
# result = df.loc[:,"column1"]
# result = df.loc[:,"column1":"column3"]
# result = df.loc[:,:"column3"]
# result = df.loc["A":"B",:"column3"]
# result = df.loc[:"B",:"column3"]
# result = df.iloc[2]
# result = df.loc["A","column3"]
# result = df.loc[["A","B"],["column1","column2"]]
# df["column4"] = pd.Series(randn(3),["A","B","C"])
# df["column5"] = df["column1"] + df["column3"]
# df.drop("column5",axis=1,inplace=True)
# print(df)
"""FILTERS"""
#data = np.random.randint(10,100,75).reshape(15,5)
#df = pd.DataFrame(data,columns=["Column1","Column2","Column3","Column4","Column5"])
# result = df.columns
# result = df.head()
# result = df.head(10)
# result = df.tail()
# #result = df.tail(10)
# result = df["Column1"].head()
# result = df.Column1.head()
# result = df[["Column1","Column2"]].head()
# result = df[5:15][["Column1","Column2"]].head()
# result = df[5:15][["Column1","Column2"]].tail()
"""FILTERS"""
# result = df[df > 50]
# result = df[df%2 ==0]
# result = df[df>50]["Column1"]
# result = df[df["Column1"]> 50][["Column1","Column2"]]
# result = df[(df["Column1"]> 50)&(df["Column1"] <=70)]
# result = df[(df["Column1"]> 50)&(df["Column2"] <=70)]
# result = df[(df["Column1"]> 50)|(df["Column2"] > 50)][["Column1","Column2"]]
# result = df.query("Column1 >50 & Column1 % 2 == 0")
# print(df)
# print("<<<<<<<<<<<<<<<<<<<<********************>>>>>>>>>>>>>>>>>>>>")
# print(result)
"""USING GROUP BY"""
# personeller = {
#     'Çalışan': ['Ahmet Yılmaz','Can Ertürk','Hasan Korkmaz','Cenk Saymaz','Ali Turan','Rıza Ertürk','Mustafa Can'],
#     'Departman': ['İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları','Bilgi İşlem','Muhasebe','İnsan Kaynakları'],
#     'Yaş': [30,25,45,50,23,34,42],
#     'Semt': ['Kadıköy','Tuzla','Maltepe','Tuzla','Maltepe','Tuzla','Kadıköy'],
#     'Maaş': [5000,3000,4000,3500,2750,6500,4500]
# }
# df = pd.DataFrame(personeller)
# result = df["Maaş"].sum()
# result = df.groupby("Departman").groups
# result = df.groupby(["Departman","Semt"]).groups
# for name,group in df.groupby("Semt"):
#     print(name)
#     print("<<<<<<<<<<<<<<<<<<<<********************>>>>>>>>>>>>>>>>>>>>")
#     print(group)
# for name,group in df.groupby("Departman"):
#     print(name)
#     print("<<<<<<<<<<<<<<<<<<<<********************>>>>>>>>>>>>>>>>>>>>")
#     print(group)
# result = df.groupby("Semt").get_group("Kadıköy")
# result = df.groupby("Departman").get_group("Muhasebe")
# result = df.groupby("Departman").sum()
# result = df.groupby("Departman").mean()
# result = df.groupby("Departman")["Maaş"].mean()
# result = df.groupby("Semt")["Yaş"].mean()
# result = df.groupby("Semt")["Çalışan"].count()
# result = df.groupby("Departman")["Yaş"].max()
# result = df.groupby("Departman")["Maaş"].max()
# result = df.groupby("Departman")["Maaş"].min()
# result = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
# result = df.groupby("Departman").agg(np.mean)
# result = df.groupby("Departman")["Maaş"].agg([np.sum,np.mean,np.max,np.min]).loc["Muhasebe"]
# print(df)
# print("<<<<<<<<<<<<<<<<<<<<********************>>>>>>>>>>>>>>>>>>>>")
# print(result)
"""WORKING ON BROKEN DATA"""
# data = np.random.randint(10,100,15).reshape(5,3)
# df = pd.DataFrame(data,index=['a','c','e','f','h'],columns=['column1','column2','column3'])
# df = df.reindex(['a','b','c','d','e','f','g','h'])
# newColumn = [np.nan, 30,np.nan,51,np.nan,30,np.nan,10]
# df["column4"] = newColumn
# result = df.drop("column1",axis=1)
# result = df.drop(["column1","column2"],axis=1)
# result = df.drop("a",axis=0)
# result = df.drop(["a","b","h"],axis=0)
# result = df.isnull()
# result = df.notnull()
# result = df.isnull().sum()
# result = df["column1"].isnull().sum()
#result = df[df["column1"].isnull()]["column1"]
#result = df[df["column1"].notnull()]
#result = df[df["column1"].notnull()]["column1"]
# result = df.dropna()#axis 0 ===> Default
# result = df.dropna(axis=1)
# result = df.dropna(how="any")
# result = df.dropna(how="all")
# result = df.dropna(subset=["column1","column2"],how="all")
# result = df.dropna(subset=["column1","column2"],how="any")
# result = df.dropna(thresh=2)
# result = df.dropna(thresh=4)#The least number of data
#df = df.fillna(value="no input")
# result = df.fillna(value=1)
# result = df.sum()
# result = df.sum().sum()
# result = df.size
# result = df.isnull().sum()
# result = df.isnull().sum().sum()
# def Mean(df):
#     total = df.sum().sum()
#     piece = df.size - df.isnull().sum().sum()
#     return total//piece
# result =df.fillna(value=Mean(df))
# print(df)
# print("<<<<<<<<<<**********>>>>>>>>>>")
# print(result)
"""USING STRING METHODS"""
#data = pd.read_csv("nba.csv")
#data.dropna(inplace=True)
# print(data.columns)
# data["Name"] = data["Name"].str.upper()
# data["Name"] = data["Name"].str.lower()
#data["index"] = data["Name"].str.find('a')
#data = data[data.Name.str.contains("Jordan")]
#data = data.Team.str.replace(" ","-")
#data[["FirstName","LastName"]] = data["Name"].loc[data["Name"].str.split().str.len()==2].str.split(expand=True)
#print(data.head(10))
"""JOIN AND MERGE"""
# customers = {
#      'CustomerId': [1,2,3,4],
#      'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#      'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }
# orders = {
#      'OrderId': [10,11,12,13],
#      'CustomerId': [1,2,5,7],
#      'OrderDate': ['2010-07-04','2010-08-04','2010-07-07','2012-07-04']
# }
# df_customers = pd.DataFrame(customers,columns=["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders,columns=["OrderId","CustomerId","OrderDate"])
# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="left")
# result = pd.merge(df_customers,df_orders,how="right")
# result = pd.merge(df_customers,df_orders,how="outer")
# print(df_customers)
# print()
# print(df_orders)
# print()
# customersA = {
#      'CustomerId': [1,2,3,4],
#      'FirstName': ["Ahmet","Ali","Hasan","Canan"],
#      'LastName': ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }
# customersB = {
#      'CustomerId': [4,5,6,7],
#      'FirstName': ["Yağmur","Çınar","Cengiz","Can"],
#      'LastName': ["Bilge","Turan","Yılmaz","Turan"]
# }
# df_customersA = pd.DataFrame(customersA,columns=["CustomerId","FirstName","LastName"])
# df_customersB = pd.DataFrame(customersB,columns=["CustomerId","FirstName","LastName"])
# result = pd.concat([df_customersA,df_customersB])#default value is zero.
# result = pd.concat([df_customersA,df_customersB],axis=1)
# print(result)
"""DATAFRAME METHODS"""
# data = {
#         "Column1":[1,2,3,4,5,],
#         "Column2":[10,20,20,45,25],
#         "Column3": ["abc","bcfa","adefd","dfdcba","ea"]
# }
# def takeSquare(x):  return x**2
# takeSquare2= lambda x: x*x
# df = pd.DataFrame(data)
# result = df["Column2"].unique()
# result = df["Column2"].nunique()
# result = df["Column2"].value_counts()
# result = df.Column1.apply(takeSquare)
# result = df.Column1.apply(takeSquare2)
# result = df.Column1.apply(lambda x: x*x)
# df["Column4"] = df.Column3.apply(len)
# result = df.columns
# result = len(df.columns)
# result = df.index
# result = len(df.index)
# result = df.info
# result = df.sort_values("Column2")
# result = df.sort_values("Column3")
# result = df.sort_values("Column2", ascending=False)
# data = {tou
#     "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
#     "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
#     "Gelir": [20,30,15,14,32,42,12,36,52]
# }
# df = pd.DataFrame(data)
# print(df.pivot_table(index="Ay",columns="Kategori",values="Gelir"))
# print(df)
# print("<<<<<<<<<<**********>>>>>>>>>>")
# print(result)
