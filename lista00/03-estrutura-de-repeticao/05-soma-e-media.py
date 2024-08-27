soma = 0

for i in range(1,6):
    n = float(input("%dº número:" % i))
    soma += n

media = soma/5
print("Soma:", soma)
print("Média:", media)