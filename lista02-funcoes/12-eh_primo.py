def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False

    return True

if __name__ == "__main__":
    n = int(input("Número:"))
    print(eh_primo(n))