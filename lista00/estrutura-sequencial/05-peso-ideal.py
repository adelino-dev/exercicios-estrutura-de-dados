altura = float(input("Digite a sua altura:"))
peso_ideal_masculino = (72.7*altura) - 58
peso_ideal_feminino = (62.1*altura) - 44.7
print("\n-- PESO IDEAL --")
print("Para homem: %.2f" % peso_ideal_masculino)
print("Para mulher: %.2f" % peso_ideal_feminino)