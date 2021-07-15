while True:
    nome = input("Digite seu nome de usuário!")
    senha = input("Sigite a senha!")
    if (senha == nome):
        print("Sua senha não pode ser igual ao nome de usuário, tente novamente!")
    else:
        break