# pip install networkx matplotlib

import networkx as nx
import matplotlib.pyplot as plt


class Grafo:
    def __init__(self):
        self.grafo = nx.DiGraph()
        print('Grafo criado.')

    def adicionar_vertice(self, nome):
        self.grafo.add_node(nome)
        print(f"Vertice {nome} adicionado ao grafo.")

    def adicionar_aresta(self, vertice1, vertice2):
        self.grafo.add_edge(vertice1, vertice2)
        print(
            f"Aresta entre vertices {vertice1} e {vertice2} adicionada ao grafo.")

    def visualizar(self):
        nx.draw(self.grafo, with_labels=True)
        plt.show()


# Cria um objeto de grafo
grafo = Grafo()

# Adiciona vertice(nós) ao grafo
grafo.adicionar_vertice("A")
grafo.adicionar_vertice("B")
grafo.adicionar_vertice("C")
grafo.adicionar_vertice("D")
grafo.adicionar_vertice("E")

# Adiciona arestas ao grafo
grafo.adicionar_aresta("A", "B")
grafo.adicionar_aresta("B", "C")
grafo.adicionar_aresta("C", "D")
grafo.adicionar_aresta("D", "A")

# Visualiza o grafo
grafo.visualizar()
