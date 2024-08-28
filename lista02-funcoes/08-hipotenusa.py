from math import sqrt

def hipotenusa(cateto1, cateto2):
    return sqrt(cateto1**2 + cateto2**2)

if __name__ == "__main__":
    c1 = float(input("Cateto 1:"))
    c2 = float(input("Cateto 2:"))

    print("\nHipotenusa:", hipotenusa(c1, c2))