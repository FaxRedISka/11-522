a = [3, 7, 2, 5, 10]
sr = sum(a)/len(a)
for i in a:
    if i < sr:
        ind = a.index(i)
        a.pop(ind)
        a.insert(ind,-1)
print(a)