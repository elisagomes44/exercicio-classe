#alunas: Ana Vitoria Cavalcante e Elisa Gomes 3ºA 
class Carro:
    def __init__ (self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 

    def ligar (self):
        print ('o carro está ligado')
        return f"{self.ligar}"
    def desligar (self):
        print ('o carro está desligado')
        return f"{self.desligar}"
    def acelerar (self):
        print ('o carro está acelerando')
        return f"{self.acelerar}"

if __name__ == "__main__":
     carro1 = Carro("jeep", "renegade","2015", "vermelho") 
     carro2 = Carro("fiat", "palio","1998","preto")
     print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor)
     print(carro1.ligar())
     print(carro1.acelerar())
     print(carro2.marca, carro2.modelo, carro2.ano, carro2.cor)
     print(carro2.ligar())
     print(carro2.marca, carro1.modelo, carro2.ano, carro1.cor)

     
    