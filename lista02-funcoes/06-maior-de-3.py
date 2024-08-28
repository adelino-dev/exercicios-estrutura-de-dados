def maior_de_3(num1, num2, num3):

    if num1 >= num2 and num1 >= num3:
        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

if __name__ == "__main__":
    n1 = int(input("Número 1:"))
    n2 = int(input("Número 2:"))
    n3 = int(input("Número 3:"))
    print("\nMaior:", maior_de_3(n1, n2, n3))