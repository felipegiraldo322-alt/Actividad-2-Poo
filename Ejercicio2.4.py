#Ejercicio 2.4. Definición de métodos con y sin valoresde retorno

import math

class Circulo:

    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (2 * self.base) + (2 * self.altura)


class Cuadrado:

    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado


class TrianguloRectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def calcular_perimetro(self):
        return (self.base + self.altura + self.calcular_hipotenusa())

    def determinar_tipo_triangulo(self):
        hipotenusa = self.calcular_hipotenusa()

        if self.base == self.altura == hipotenusa:
            return "Equilátero"

        elif self.base == self.altura:
            return "Isósceles"

        elif self.base == hipotenusa:
            return "Isósceles"

        elif self.altura == hipotenusa:
            return "Isósceles"

        else:
            return "Escaleno"

class Rombo:

    def __init__(self, lado, diagonal_mayor, diagonal_menor):
        self.lado = lado
        self.diagonal_mayor = diagonal_mayor
        self.diagonal_menor = diagonal_menor

    def calcular_area(self):
        return (self.diagonal_mayor * self.diagonal_menor) / 2

    def calcular_perimetro(self):
        return 4 * self.lado

class Trapecio:

    def __init__(self, base_mayor, base_menor, altura, lado1, lado2):
        self.base_mayor = base_mayor
        self.base_menor = base_menor
        self.altura = altura
        self.lado1 = lado1
        self.lado2 = lado2

    def calcular_area(self):
        return ((self.base_mayor + self.base_menor) * self.altura) / 2

    def calcular_perimetro(self):
        return (self.base_mayor + self.base_menor + self.lado1 + self.lado2)

class PruebaFiguras:

    @staticmethod
    def main():

        figura1 = Circulo(2)

        figura2 = Rectangulo(1, 2)

        figura3 = Cuadrado(3)

        figura4 = TrianguloRectangulo(3, 5)

        figura5 = Rombo(5, 8, 6)

        figura6 = Trapecio(10, 6, 4, 5, 5)

        #Circulo
        print("El área del círculo es =", figura1.calcular_area())
        print("El perímetro del círculo es =", figura1.calcular_perimetro())
        print()

        #Rectángulo
        print("El área del rectángulo es =", figura2.calcular_area())
        print("El perímetro del rectángulo es =", figura2.calcular_perimetro())
        print()

        #Cuadrado
        print("El área del cuadrado es =", figura3.calcular_area())
        print("El perímetro del cuadrado es =", figura3.calcular_perimetro())
        print()

        #Triángulo
        print("El área del triángulo es =", figura4.calcular_area())
        print("La hipotenusa del triángulo es =", figura4.calcular_hipotenusa())
        print("El perímetro del triángulo es =", figura4.calcular_perimetro())
        print("El tipo de triángulo es =", figura4.determinar_tipo_triangulo())
        print()

        #Rombo
        print("El área del rombo es =", figura5.calcular_area())
        print("El perímetro del rombo es =", figura5.calcular_perimetro())
        print()

        #Trapecio
        print("El área del trapecio es =", figura6.calcular_area())
        print("El perímetro del trapecio es =", figura6.calcular_perimetro())
        print()

if __name__ == "__main__":
    PruebaFiguras.main()