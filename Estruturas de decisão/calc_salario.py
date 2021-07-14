salario = float(input("Digite o valor do salario!"))
ir = 0
salario_bruto = salario
fgts = 0.08
inss = 0
if salario<1903.98:
    ir = 0
elif salario>=1903.99 and salario <= 2826.65:
    ir = 0.075
elif salario>=2826.66 and salario <=3751.05:
    ir = 0.15
elif salario>=3751.06 and salario <=4664.68:
    ir = 0.225
else:
    ir = 0.275

if salario<1045:
    inss = 0.075
elif salario>=1045.01 and salario <= 2089.60:
    inss = 0.09
elif salario>=2089.61 and salario <= 3134.40:
    inss = 0.12
elif salario >= 3134.41 and salario <=6101.06:
    inss = 0.14
else:
    inss = (((6101.06*0.14)*100/6101.06)/100)

desconto_ir = salario*ir
desconto_inss = salario*inss
desconto_fgts = salario*fgts

print(f"Salario Bruto: R$ {salario_bruto}")
print("IR {:.1f}%           R$ {:.2f}".format((100*ir), desconto_ir))
print("INSS {:.1f}%         R$ {:.2f}".format((inss*100), desconto_inss))
print("FGTS {:.0f}%            R$ {:.2f}".format((fgts*100), desconto_fgts))
print("Total de descontos R$ {:.2f}".format((salario*ir) + (salario*inss)))
salario = salario - (salario*inss) - (salario*ir) 
print(f"Salário líquido    R$ {salario}")