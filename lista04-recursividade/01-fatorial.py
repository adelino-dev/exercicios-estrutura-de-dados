def fatorial(num):
    if num in (0, 1):
        return 1
    
    return num * fatorial(num-1)

if __name__ == "__main__":
    num = int(input("Número:"))
    print("Fatorial:", fatorial(num))