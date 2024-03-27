while True:
    s = input()    
    d = {}

    for i in str:
        if d.get(i) is None:
            d[i] = 1
        else:
            d[i] += 1

    print(d)
