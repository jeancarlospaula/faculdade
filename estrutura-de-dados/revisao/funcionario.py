class Funcionario:
    def __init__(self, nome, idade, cargo, salario):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        aumento = self.salario * porcentagem / 100
        self.salario += aumento

    def mostrar_informacoes(self):
        print("Nome recebido foi: ", self.nome)
        print("Idade recebida foi: ", self.idade)
        print("Cargo recebido foi: ", self.cargo)
        print("Salario recebido foi: ", self.salario)


funcionario1 = Funcionario("Matheus", 23, "Aux. Adm", 1300)
funcionario2 = Funcionario("Jean", 19, "Estagiário", 1300)

funcionario1.mostrar_informacoes()
