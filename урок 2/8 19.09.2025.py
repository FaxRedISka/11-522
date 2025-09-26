a = [1231,24,123,41,235,325,4,87,68,56,5,63,45,3,4,5]
z = 0
for i in a:
    if i>z:
        z = i

c = a[0]
for i in a:
    if i<c:
        c = i
z1 = a.index(z)
c1 = a.index(c)
a.pop(z1)
a.insert(z1,c)
a.pop(c1)
a.insert(c1,z)
print(a)
