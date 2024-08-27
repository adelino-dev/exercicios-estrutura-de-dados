l1 = float(input("Lado 1:"))
l2 = float(input("Lado 2:"))
l3 = float(input("Lado 3:"))

#Analisa se os valores podem ser de um triângulo:

if (l1+l2) > l3 and (l1+l3) > l2 and (l2+l3) > l1:
    print("Os valores podem ser de um triângulo.")

    #Analisa qual o tipo de triângulo:
    if l1 == l2 and l2 == l3:
        tipo_triangulo = "Equilátero"
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo_triangulo = "Isóceles"
    else:
        tipo_triangulo = "Escaleno"
    
    print("Tipo: Triângulo "+tipo_triangulo)

else:
    print("Não pode ser um triãngulo.")