nota1 = float(input("Digite a primeira nota de 0 a 10"))
nota2 = float(input("Digite a segunda nota!"))


media = (nota1+nota2)/2

if media>=7:
    print("Aprovado!")
elif media <7:
    print("Reprovado!")
elif media == 10:
    print("Aprovado com Distinção!")
