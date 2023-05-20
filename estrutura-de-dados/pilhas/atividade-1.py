class Pilha:
    def __init__(self):
        self.pilha = []
        print("Pilha criada.")

    def empilhar(self, elemento):
        self.pilha.insert(0, elemento)
        print(f"O elemento {elemento} foi adicionado ao topo da pilha.")
        print("Pilha atualizada:")
        self.elementos()

    def elementos(self):
        if not self.pilha:
            print("A pilha não possui elementos.")
        else:
            for elemento in self.pilha:
                print(elemento)


pilha = Pilha()

pilha.empilhar(10)
pilha.empilhar(20)
pilha.empilhar(30)
