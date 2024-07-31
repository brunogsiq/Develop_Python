trabalhador = 'Bruno'
valorHora = 4
dias = 30
horasTrabalhadas = 8

salarioMensal = valorHora * horasTrabalhadas * dias

# Com apenas 1 zero
print(str(trabalhador) + ' receberá o valor de: ' + str(float(salarioMensal)))

# Usando format
print(str(trabalhador) + ' receberá o valor de: ' + '{:.2f}'.format(salarioMensal))

# Usando f-string
print(f'{trabalhador} receberá o valor de: {salarioMensal:.2f}')