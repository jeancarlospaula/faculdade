class Time():
    def __init__(self, nome, jogadores):
        self.nome = nome
        self.jogadores = jogadores
        print(f"Time '{nome}' criado.")

    def adicionaJogadores(self, numero, nome):
        self.jogadores.append([numero, nome])
        print(f"Jogador {nome}, camisa {numero}, adicionado.")

    def imprimeJogadores(self):
        print(f"Lista de jogadores do time {self.nome}:")
        for jogador in self.jogadores:
            numeroJogador = jogador[0]
            nomeJogador = jogador[1]
            print(f"Camisa {numeroJogador} - {nomeJogador}")


nomeTime = 'Amigos do Jean'
listaJogadores = [
    [1, 'Jean'],
    [2, 'Tião'],
    [3, 'Gerônimo']
]

novoTime = Time(nomeTime, listaJogadores)

novoTime.adicionaJogadores(4, 'Juca')
novoTime.imprimeJogadores()
