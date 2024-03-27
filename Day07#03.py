L = list(range(0,10))
L1 = L2 = []

for i in L:
    m = i%2
    if m == 0:
        L2 = L2 + [i]
    else:
        L1 = L1 + [i]

L = L1 + L2
print(L)
