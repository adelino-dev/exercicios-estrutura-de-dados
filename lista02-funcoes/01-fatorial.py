def fatorial(n):
    fatorial = 1
    for i in range(2, n+1):
        fatorial *= i

    return fatorial

if __name__ == '__main__':
    n = int(input("Digite um núemro:"))
    print("Fatorial:", fatorial(n))