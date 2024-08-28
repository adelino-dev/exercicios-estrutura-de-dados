def eh_par(numero):
    if numero%2 == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    n = int(input("Digite um número:"))
    print(eh_par(n))