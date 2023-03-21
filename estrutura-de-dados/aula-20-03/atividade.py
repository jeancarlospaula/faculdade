import os

itens = list()

while True:
    opcao = input(
        'Selecione uma opção - criar [c], listar [l], atualizar [a], deletar [d] e sair [s]: ')

    if opcao == 'c':
        item = input('Digite um item: ')
        itens.append(item)
        print('Item inserido.')
    elif opcao == 'l':
        if len(itens) == 0:
            print('Não existem itens salvos.')

        for item in itens:
            print(item)
            print('-'*5)
    elif opcao == 's':
        print('Sistema encerrado.')
        break
    elif opcao == 'd':
        try:
            posicao = int(input('Digite o índice do item para deletar: '))

            if posicao < 0 or posicao > len(itens) + 1:
                print('Não existe um item para o índice informado.')
                continue
        except:
            print('O valor informado não foi um número.')
            continue

        del (itens[posicao])
        print('Item deletado.')
    elif opcao == 'a':
        try:
            posicao = int(input('Digite o índice do item para atualizar: '))

            if posicao < 0 or posicao > len(itens) + 1:
                print('Não existe um item para o índice informado.')
                continue
        except:
            print('O valor informado não foi um número.')

        novoValor = input('Digite o novo valor para o índice informado: ')

        itens[posicao] = novoValor
        print('Item atualizado.')
    else:
        print('Opção informada não existe.')
