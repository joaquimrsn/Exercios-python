populacaoA= 80000
populacaoB = 200000
taxaA = 1.03
taxaB = 1.015
ano = 0

while(populacaoA <= populacaoB):
    populacaoB = populacaoB*taxaB
    populacaoA = populacaoA*taxaA
    ano = ano+1

print("Foram necessários {:.0f} anos até que a População A {:.0f} habitantes ultrapassasse a população B {:.0f} habitantes.".format(ano, populacaoA, populacaoB))