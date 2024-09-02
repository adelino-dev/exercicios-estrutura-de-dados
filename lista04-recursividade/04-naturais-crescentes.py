def imprimirNaturais(n):
    if n < 0:
        return 
    elif n == 0:
        print(n)
    else:
        imprimirNaturais(n - 1)
        print(n)

if __name__ == "__main__":
    n = int(input("Número:"))
    imprimirNaturais(n)