def contarLetra(letra, palavra):
    num = 0
    if len(palavra) == 1:
        if letra == palavra[-1]:
            return 1
        else:
            return 0
    else:
        if letra == palavra[-1]:
            return 1 + contarLetra(letra, palavra[0:-1])
        else:
            return 0 + contarLetra(letra, palavra[0:-1])


if __name__ == "__main__":
    palavra = input("Palavra:")
    letra = input("Letra:")

    print(contarLetra(letra, palavra))
