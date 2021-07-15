populacaoA = int(input("Digite a população da primeira cidade:")) 
taxaA = int(input("Digite a taxa de crescimento da população em porcentagem:"))
taxaA = (taxaA/100)+1

populacaoB = int(input("Digite a população da segunda cidade: "))
taxaB = int(input("Digite a taxa de crescimento da população em porcentagem:"))
taxaB = (taxaB/100)+1
ano = 0


while(populacaoA <= populacaoB):
    populacaoB = populacaoB*taxaB
    populacaoA = populacaoA*taxaA
    ano = ano+1

print("Foram necessários {:.0f} anos até que a População A {:.0f} habitantes ultrapassasse a população B {:.0f} habitantes.".format(ano, populacaoA, populacaoB))