while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if (operacao == "+"):
            resultado = numero1 + numero2
        elif (operacao == "-"):
            resultado = numero1 - numero2
        elif (operacao == "*"):
            resultado = numero1 * numero2
        elif (operacao == "/"):
            resultado = numero1 / numero2
        else:
            print("Operação inválida!")
            continue

        print(f"{numero1} {operacao} {numero2} = {resultado}")

        if (input("Deseja sair? (s/n): ") == "s"):
            print("Saindo do sistema...")
            break
    except:
        print("Ocorreu um erro. Digite apenas números!")
        continue
