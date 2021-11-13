import pandas as pd

student = pd.Series(["Ali",21,"CE"],index=["Name","Age","Department"])
student.name = "hasan ali özkan"
# X = "Ali" in student.values
# print(X)
# X = "Name" in student
# print(X)
# Y = "Job" in student
# print(Y)
# print(student)
# print(student.values)
# print(student.index)
# print(student.shape)
# print(student.ndim)
# print(student.size)
# print(student.name)
# print(student.dtype)
# print(len(student))
# print(list(student))
# print(dict(student))
# print(sorted(student))
"""file = open("Deneme.txt","w")

for i in range(0,1000):
    file.write(str(data[i]))
    file.write("\n")

file.close()


data = pd.read_csv("ReviewContent.csv",usecols=["Review ID"]
                   ,squeeze=True,encoding="UTF-8",engine="python")#if the squeeze parameter is true the type is Serie
"""                                                                  #else the type is DataFrame
newdata = pd.read_csv("ReviewContent.csv",encoding="UTF-8",engine="python")
"""
sortingByValues = data.head(10).sort_values(ascending=False)
sortingByIndex = data.head(10).sort_index(ascending=False)
print(sortingByValues)
print()
print(sortingByIndex)
withoutGet = data[1001]
withGet = data.get(1001)
print(withoutGet)
print(withGet)
withGet = data.get(1001,default="There is not this index!!!!")
print(withGet)
withGet = data.get([0,1])
print(withGet)
"""
df = pd.DataFrame(newdata,columns=["Review ID","Review Content"])
df["hasanali"] = len(df["Review Content"])
newRow = pd.DataFrame({"Review ID":12443673932,"Review Content":"Everything was beatiful."},index=[1000])
df = df.append(newRow)
print(df)
df.pop("Review ID")
print(df)
