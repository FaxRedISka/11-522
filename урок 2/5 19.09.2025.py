a = [1231,24,123,41,235,325,4,87,68,56,5,63,45,3,4,5]
z = 0
for i in a:
    if i>z:
        z = i
print(z)
z = a[0]
for i in a:
    if i<z:
        z = i
print(z)