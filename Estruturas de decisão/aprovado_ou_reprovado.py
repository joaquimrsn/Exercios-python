nota1 = float(input("Digite a primeira nota!"))
nota2 = float(input("Digite a segunda nota!"))


media = (nota1+nota2)/2

if media>0 and media <4:
    conceito = "E"
elif media>=4 and media <6:
    conceito = "D"
elif media >=6 and media <7.5:
    conceito = "C"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >=9 and media <=10:
    conceito = "A"

if conceito == "A" or conceito == "B" or conceito == "C":
    print(f"Conceito {conceito}, APROVADO!")
else:
    print(f"Conceito {conceito}, REPROVADO!")
