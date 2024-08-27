maior = 0

for i in range(1,6):
    n = float(input("%dº número:" % i))

    if i == 1:
        maior = n
    
    if n > maior:
        maior = n

print("\nMaior número:", maior)