x = [1, 2, 3 ,4 ,5, 6, 7]
fim = len(x) -1


for i in range(len(x)//2):
    aux = x[i]
    x[i] = x[fim]
    x[fim] = aux
    fim -= 1

print(x)

