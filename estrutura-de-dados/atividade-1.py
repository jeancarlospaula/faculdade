nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = input('Digite sua idade: ')
peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')


print('---------------------')
print('Nome='+nome)
print('Sobrenome='+sobrenome)
print('Idade='+idade)
print('Peso='+peso)
print('Altura='+altura)
print('---------------------')

if int(idade) >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')