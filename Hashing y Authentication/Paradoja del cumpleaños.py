print('Num. probabilidad')
p = 1
for i in range(1, 80):
    p = p * (366 - i) / 365
    print(f'{i}: {(1-p):.3f}')