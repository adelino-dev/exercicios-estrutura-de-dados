def eh_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def eh_data_valida(dia, mes, ano):
    if mes > 12 or mes < 1:
        return False
    
    elif dia > 31 or dia < 1:
        return False
    
    elif mes in (2, 4, 6, 9, 11) and dia > 30:
        return False

    elif mes == 2 and dia > 29:
        return False
    
    elif mes == 2 and not(eh_bissexto(ano)) and dia>28:
        return False
    
    else:
        return True

if __name__ == "__main__":
    dia = int(input("Dia:"))
    mes = int(input("Mês:"))
    ano = int(input("Ano:"))

    print(eh_data_valida(dia, mes, ano))