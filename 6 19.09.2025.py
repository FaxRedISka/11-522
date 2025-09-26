a = [1,1,1,1,1,12,3,23,2,234,23,34,53,4]
c = []
for i in a:
    if i not in c:
        c.append(i)
print(c)