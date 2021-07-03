num_int1 = (int(input("Digite um número inteiro! ")))
num_int2 = (int(input("Digite outro numero inteiro!")))
num_float  = float(input("Digite um valor real!"))

produto_dobro = (num_int1*2)*(num_int2/2)
soma_triplo = (num_int1*3)+num_float
elevado = num_float**3

print("O produto do dobro do primeiro numero com metade do segundo é igual a {}, a soma do triplo do primeiro com o terceiro é {} e o terceiro elevado ao cubo é {}".format(produto_dobro, soma_triplo, elevado))