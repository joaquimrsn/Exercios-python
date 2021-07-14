turno = input("Digite: M-Matutino, V-Vespertino e N-Noturno!")
turno = turno.upper()
if turno == "M":
    print("Bom dia!")
elif turno == "V":
    print("Boa tarde!")
elif turno == "N":
    print("Boa noite!")
else:
    print("Valor inválido!")