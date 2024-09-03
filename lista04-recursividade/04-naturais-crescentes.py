    def imprimirNaturais(n):
        if n == 0:
            print(0)
        else:
            imprimirNaturais(n-1)
            print(n)

    if __name__ == "__main__":
        n = int(input("Número:"))
        imprimirNaturais(n)