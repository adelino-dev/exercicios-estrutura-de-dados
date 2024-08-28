def maior_de_2(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

if __name__ == "__main__":
    n1 = int(input("Número 1:"))
    n2 = int(input("Número 2:"))
    print("\nMaior:", maior_de_2(n1, n2))