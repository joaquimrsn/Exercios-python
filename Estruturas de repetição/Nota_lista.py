
while True:
    nota = int(input("Digite uma nota de 0 a 10!"))
    if (nota<0 or nota>10):
        print("Valor inválido!")
    else:
        print(f"A nota é {nota}")
        break