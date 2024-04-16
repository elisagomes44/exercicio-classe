class Pedido:
    def __init__ (self, itens, pagamento, status):
        self.itens = itens
        self.pagamento = pagamento
        self.status = status

    def depositar (self): 
        return f'{self.numero_da_conta} está depositando dinheiro'
    def sacar (self): 
        return f'{self.titular} está sacando dinheiro'
    def saldo_atual (self):
        return f'{self.saldo} este é o saldo atual'
    
if __name__ == "__main__":
     conta = Conta_Bancaria ("09062006","2500", "Eloyse")
     print(conta.depositar())
     print(conta.sacar())
     print(conta.saldo_atual())