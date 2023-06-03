class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, vertice_origem, vertice_destino):
        if vertice_origem in self.vertices and vertice_destino in self.vertices:
            self.vertices[vertice_origem].append(vertice_destino)
            self.vertices[vertice_destino].append(vertice_origem)

    def exibir_grafo(self):
        for vertice in self.vertices:
            print(vertice + ": " + ", ".join(self.vertices[vertice]))


# Criando um objeto de grafo
grafo = Grafo()

# Adicionando vértices
grafo.adicionar_vertice("A")
grafo.adicionar_vertice("B")
grafo.adicionar_vertice("C")
grafo.adicionar_vertice("D")

# Adicionando arestas
grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("B", "C")
grafo.adicionar_aresta("C", "D")
grafo.adicionar_aresta("D", "A")

# Exibindo o grafo
grafo.exibir_grafo()
