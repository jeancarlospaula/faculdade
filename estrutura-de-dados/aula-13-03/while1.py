sistema = True

while sistema:
    nome = input("Digite seu nome: ")

    if (nome == "sair"):
        print("Saindo do sistema...")
        break

    print(f"Olá {nome}!")
