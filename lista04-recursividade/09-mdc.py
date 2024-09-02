def MDC(a, b):
    if (b != 0):
       return MDC(b, (a%b))
    else:
        return a

if __name__ == "__main__":
    a = int(input("Digite o valor de A:"))
    b = int(input("Digite o valor de B:"))
    print(f'\nMDC({a}, {b}) = {MDC(a, b)}')
