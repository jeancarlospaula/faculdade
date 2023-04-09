lista = []

i = 0
while i < 5:
    i = i + 1
    num = int(input(f'Digite o {i}º número: '))
    lista.append(num)

soma = 0
for item in lista:
    soma += item

print(f'Soma: {soma}')
