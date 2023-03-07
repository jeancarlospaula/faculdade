print('----- MAIOR NÚMERO -----')

numero1 = int(input('Digite o primeiro número: '))
numero2 = int(input('Digite o segundo número: '))

if numero1 == numero2:
    print('Os números são iguais')
elif numero1 > numero2:
    print('O maior número é: ' + str(numero1))
else:
    print('O maior número é: ' + str(numero2))
