for i in range(2, 19+1):
    for j in range(1, 19+1):
        if i % 2 != 0:
            print(i, 'X', j, '=', int(i*j))
