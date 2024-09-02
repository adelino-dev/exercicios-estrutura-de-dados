def fatorial_duplo(num):
    if num == 1:
        return 1
    
    elif num%2 == 0:
        return fatorial_duplo(num-1)
    
    else:
        return num * fatorial_duplo(num-2)

if __name__ == "__main__":
    num = int(input("Número:"))
    print("Fatorial Duplo:", fatorial_duplo(num))