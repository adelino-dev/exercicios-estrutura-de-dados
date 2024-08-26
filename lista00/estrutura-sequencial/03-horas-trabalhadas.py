salario_hora = float(input("Quanto você ganha por hora?"))
horas_por_mes = float(input("Quantas horas você trabalhou no mês?"))

salario_mes = salario_hora * horas_por_mes
print("\nSalário do mês: R$%.2f" % salario_mes)