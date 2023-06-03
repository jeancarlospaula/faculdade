# pip install networkx matplotlib


import networkx as nx
import matplotlib.pyplot as plt

# Cria um objeto de grafo direcionado
grafo = nx.DiGraph()

# Adiciona nós ao grafo
grafo.add_node("A")
grafo.add_node("B")
grafo.add_node("C")
grafo.add_node("D")

# Adiciona arestas ao grafo
grafo.add_edge("A", "B")
grafo.add_edge("B", "C")
grafo.add_edge("C", "D")
grafo.add_edge("D", "A")

# Visualiza o grafo
nx.draw(grafo, with_labels=True)
plt.show()
