def inverter(palavra):
    if len(palavra) == 1:
        return palavra
    
    return palavra[-1] + inverter(palavra[0:-1])

if __name__ == "__main__":
    palavra = input("Digite uma palavra:")
    print(inverter(palavra))