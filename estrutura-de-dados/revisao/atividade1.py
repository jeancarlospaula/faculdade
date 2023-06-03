class Produto:
    def __init__(self, codigo, nome, preco, estoque):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_preco(self, preco):
        self.preco = preco

    def adicionar_estoque(self, quantidade):
        self.estoque += quantidade

    def remover_estoque(self, quantidade):
        self.estoque -= quantidade

    def mostrar_informacoes(self):
        print("Codigo = ", self.codigo)
        print("Nome = ", self.nome)
        print("Preco = ", self.preco)
        print("Estoque = ", self.estoque)


produto1 = Produto(123, "Produto 1", 1500, 5)
produto1.atualizar_preco(678)
produto1.adicionar_estoque(4)
produto1.remover_estoque(2)
produto1.mostrar_informacoes()
