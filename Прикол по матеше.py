print('p q r s   f   z')
a = 1
for p in 0, 1:
    for q in 0, 1:
        for r in 0, 1:
            for s in 0,1:
                f = (p <= q) <= (r <= s)
                z = (p <= r) <= (q <= s)
                print(p,q,r, s, f , z)
                if not(f == z):
                    a = 0
if a == 1:
    print('Эквивалентны')
else:
    print('Не эквивалентны')






