import requests as rq
import json
url = "https://api.exchangeratesapi.io/latest?base="
doviz1 = input("Bozulan döviz türü:").upper()
doviz2 = input("Alınan döviz türü:").upper()
miktar = int(input(f"Ne kadar {doviz1} bozdurmak istiyorsunuz?:"))

result = rq.get(url+doviz1)
result = json.loads(result.text)

print("1 {0} = {1} {2}".format(doviz1,result['rates'][doviz2],doviz2))
print("{0} {1} = {2}".format(miktar,doviz1,miktar*result['rates'][doviz2],doviz2))
