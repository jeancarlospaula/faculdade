lista = [4, 8, 12]


def calcularMedia(lista):
    tamanhoLista = len(lista)
    somaItens = 0

    for item in range(tamanhoLista):
        somaItens += lista[item]

    mediaItens = somaItens / tamanhoLista
    print(f"A média dos itens da lista é {mediaItens}")


calcularMedia(lista)
