def fibonacci(termo):
    if termo <= 1:
        return 0
    else:
        sequencia = [0,1]
        soma = 1
        for i in range(2, termo):
            n = sequencia[-2] + sequencia[-1]
            sequencia.append(n)
            soma += n

        return soma

if __name__ == "__main__":
    num = int(input("Número:"))
    print(fibonacci(num))