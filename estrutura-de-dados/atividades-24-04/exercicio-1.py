class ContaBancaria():
    def __init__(self, numeroConta, nomeTitular, saldo):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo
        print(f"Conta bancária criada. Saldo inicial R${saldo}")

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor} realizado.")

    def sacar(self, valor):
        if valor > self.saldo:
            print(
                f"Saque de R${valor} não realizado. Saldo de R${self.saldo} insuficiente.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor} realizado.")

    def mostrarExtrato(self):
        print(f"O saldo da sua conta é R${self.saldo}")


novaConta = ContaBancaria(12345, 'Jean de Paula', 1200)

novaConta.depositar(50)
novaConta.mostrarExtrato()

novaConta.sacar(1000)
novaConta.mostrarExtrato()

novaConta.sacar(300)
