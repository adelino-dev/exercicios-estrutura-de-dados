def dia_da_semana(dia):
    match dia:
        case 1:
            return "Domingo"
        case 2:
            return "Segunda"
        case 3:
            return "Terça"
        case 4:
            return "Quarta"
        case 5:
            return "Quinta"
        case 6:
            return "Sexta"
        case 7:
            return "Sábado"
        case _:
            return "Valor inválido"

if __name__ == "__main__":
    n = int(input("Número do dia:"))
    print(dia_da_semana(n))