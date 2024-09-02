def imprimirNaturais(n):
    if n == 0:
        print(0)
    else:
        print(n)
        imprimirNaturais(n-1)

if __name__ == "__main__":
    n = int(input("Número:"))
    imprimirNaturais(n)