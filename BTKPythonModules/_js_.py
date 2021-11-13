import json

personString = '{"name":"Ali","languages":["Python",",C#"]}'
persondict = {"name":"Ali","languages":["Python",",C#"]}
persondict = json.loads(personString)
result = json.dumps(persondict,indent=4,sort_keys=True)
print(result)



#result = json.loads(personString)
"""
with open("person.json") as f:
    data = json.load(f)
    print(data["name"])
    print(data["languages"])
    
result = json.dumps(persondict)
print(result)

with open("person.json","w") as f:
    json.dump(persondict,f)
"""


