while True:
    nome = input("Digite o seu nome!")
    if len(nome) <3:
        print("Seu nome deve ter pelo menos 3 caracteres.")
    else: 
        break
while True:

    idade = int(input("Digite a sua idade!"))
    if idade<0 and idade>150:
        print("Idade inválida!")
    else:
        break

while True:
    salario = float(input("Digite o valor do seu salário!"))
    if salario<0:
        print("Salário deve ser maior que 0:")

    else:
        break
    
while True:
    sexo = input("Sexo: f ou m?")
    if(sexo.lower() != "f" and sexo.lower() != "m"):
        print("Sexo inválido!")
    else:
        break

while True:

    est_civil = input("Estado Civíl: s- solteio(a), c-casado(a), v-viúvo(a), d-divorciado(a)")

    if(est_civil.lower() != "s" and est_civil.lower() != "c" and est_civil.lower() != "v" and est_civil.lower() != "d"):
        print("Estado civíl inválido!")
    else:
        break
    
print("Nome:", nome)
print("Idade:", idade)
if (sexo == "m"):
    print("Sexo Masculino")
else:
        print("Sexo Feminino")
if (est_civil == "s"):
        print("Estado Civil: Solteiro")
elif(est_civil == "c"):
    print("Estado Civil: Casado")
elif(est_civil == "v"):
    print("Estado Civil: Viúvo")
else:
    print("Estado Civil: Divorciado.")
    