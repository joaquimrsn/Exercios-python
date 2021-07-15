numeros = []
contador = 0
while(contador<5):
    valores = int(input(f"Digite o valor {contador+1}: "))
    numeros.append(valores)
    contador = contador+1
maior = numeros[0]
for e in numeros:
    if e > maior:
        maior = e
print("O maior valor é: ", maior)