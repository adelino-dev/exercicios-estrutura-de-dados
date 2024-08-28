def soma_numeros(numero):
    soma = numero
    for i in range(1, numero):
        soma += i
    return soma

if __name__ == '__main__':
    n  = int(input("Número:"))
    print(soma_numeros(n))