#alunas: Ana Vitoria Cavalcante e Elisa Gomes 3ºA
class Estudante: 
    def __init__ (self, nome, idade, notas):
        self.nome = nome
        self.idade = idade
        self.notas = notas

    def calcular_media (self): 
        return f'{self.nome}, {self.idade}, {self.altura}, são as informações de {self.nome}'
    def cumprimentar (self): 
        return f'{self.nome} está cumprimentando alguém: Olá, como vai?'
    
if __name__ == "__main__":
     estudante1= Estudante ("Elisa", "16 anos", "1,62")
     print (estudante1.informacoes())
     print (estudante1.cumprimentar())