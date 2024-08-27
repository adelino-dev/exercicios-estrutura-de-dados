nota = float(input("Nota:"))

while nota < 0 or nota > 10:
    print("\nValor inválido! Digite um valor entre 0 e 10.")
    nota = float(input("Nota:"))

print("\nValor válido!")