"""def in_array(array1, array2):
    r = []
    string = ""
    for item in array2:
        string = string + " " + item
    for it in array1:
        if it in string:
            r.append(it)
    r.sort()
    for word in r:
        if r.count(word) !=1:
            r.remove(word)
    return r





a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
r = ['arp', 'live', 'strong']
print(in_array(a1, a2))
"""

