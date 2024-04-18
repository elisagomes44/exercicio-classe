#Alunas: Ana Vitória Cavalcante e Elisa Gomes 3ºA
class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3
    
    def calcular_area(self):
        # Calculando a área usando a fórmula de Heron
        s = self.calcular_perimetro() / 2
        area = (s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3)) ** 0.5
        return area

