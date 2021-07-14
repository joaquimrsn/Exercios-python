salario = float(input("Digite o valor do seu salário!"))
salario_inicial = salario

if salario>0 and salario<280:
    percentual = 0.20
elif salario>=280 and salario <700:
    percentual = 0.15
elif salario >=700 and salario<1500:
    percentual = 0.10
else:
    percentual = 0.05

aumento = salario*percentual
salario = salario+aumento
percentual = percentual*100

print("O salário inicial era R$ {}, com o aumento de {}%, equivalente a R$ {:.2f}, passou a ser R$ {}".format(salario_inicial, percentual, aumento, salario))

