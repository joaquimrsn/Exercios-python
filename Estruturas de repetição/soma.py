numeros = []
contador = 0
while(contador<5):
    valores = int(input(f"Digite o valor {contador+1}: "))
    numeros.append(valores)
    contador = contador+1
soma = 0
for e in numeros:
    soma = soma+e
print("A soma dos valores é:", soma)