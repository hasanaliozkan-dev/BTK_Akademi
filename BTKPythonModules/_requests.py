import requests as rq
import json
#print(rq.__file__)
#result = dir(rq)
"""result = rq.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)
for i in result:
    if i["userId"] == 1:
        print(i["title"])
print(result[0])"""

"""result = rq.get("https://obs.mu.edu.tr/oibs/ogrenci/login.aspx").text
with open("obshtml.txt","w") as file:
    file.write(result)
print(result)
"""
