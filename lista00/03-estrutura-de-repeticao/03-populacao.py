populacao_A = 80000
populacao_B = 200000

taxa_crescimento_A = 0.03
taxa_crescimento_B = 0.015

anos = 0

while populacao_A < populacao_B:
    populacao_A += populacao_A * taxa_crescimento_A
    populacao_B += populacao_B * taxa_crescimento_B
    anos += 1

print("%d anos" % anos)