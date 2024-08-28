data = input("Digite uma data (no formato dd/mm/aaaa):")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6::])

eh_data_valida = True

# Analisa se a data é válida
if mes > 12 or mes < 1:
    eh_data_valida = False

elif dia > 31 or dia < 1:
    eh_data_valida = False

elif mes in (2, 4, 6, 9, 11) and dia > 30:
    eh_data_valida = False

elif mes == 2 and dia > 29:
    eh_data_valida = False

elif mes == 2:
    # Verifica se é ano bissexto
    eh_bissexto = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    
    if eh_bissexto and dia > 29:
        eh_data_valida = False
    elif not eh_bissexto and dia > 28:
        eh_data_valida = False


#Mostra se a data é válida ou não:
if eh_data_valida:
    print("A data é válida.")
else:
    print("A data NÃO é válida.")