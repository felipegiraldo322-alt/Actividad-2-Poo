#Ejercicio 2.3. Estado de un objeto

from enum import Enum

class TipoA(Enum):
    CIUDAD = "CIUDAD"
    SUBCOMPACTO = "SUBCOMPACTO"
    COMPACTO = "COMPACTO"
    FAMILIAR = "FAMILIAR"
    EJECUTIVO = "EJECUTIVO"
    SUV = "SUV"

class TipoColor(Enum):
    BLANCO = "BLANCO"
    NEGRO = "NEGRO"
    ROJO = "ROJO"
    NARANJA = "NARANJA"
    AMARILLO = "AMARILLO"
    VERDE = "VERDE"
    AZUL = "AZUL"
    VIOLETA = "VIOLETA"

class TipoCom(Enum):
    GASOLINA = "GASOLINA"
    BIOETANOL = "BIOETANOL"
    DIESEL = "DIESEL"
    BIODIESEL = "BIODIESEL"
    GAS_NATURAL = "GAS_NATURAL"

class Automovil:

    def __init__(self, marca: str, modelo: int, motor: int,
                 tipo_combustible: TipoCom, tipo_automovil: TipoA,
                 numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, automatico: bool,
                 color: TipoColor, multas=0):

        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.automatico = automatico
        self.multas = multas
        self.color = color

    def acelerar(self, incremento_velocidad: int):
        self.velocidad_actual += incremento_velocidad

        if self.velocidad_actual > self.velocidad_maxima:
            self.multas += 1

    def desacelerar(self, decremento_velocidad: int):
        if (self.velocidad_actual - decremento_velocidad) >= 0:
            self.velocidad_actual -= decremento_velocidad

        else:
            print("No se puede decrementar a una velocidad negativa")

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia: int) -> float:
        if self.velocidad_actual == 0:
            return float('inf')

        return distancia / self.velocidad_actual

    def numero_multas(self) -> int:
        if self.multas < 0:
            return 0

        return self.multas

    def imprimir(self):
        print(f"Marca = {self.marca}")
        print(f"Modelo = {self.modelo}")
        print(f"Motor = {self.motor}")
        print(f"Tipo de combustible = {self.tipo_combustible.value}")
        print(f"Tipo de automóvil = {self.tipo_automovil.value}")
        print(f"Número de puertas = {self.numero_puertas}")
        print(f"Cantidad de asientos = {self.cantidad_asientos}")
        print(f"Velocidad máxima = {self.velocidad_maxima}")
        print(f"Numero de multas = {self.multas}")
        print(f"Automático = {'Sí' if self.automatico else 'No'}")
        print(f"Color = {self.color.value}")

if __name__ == "__main__":

    auto1 = Automovil(
        "Ford", 2018, 3, TipoCom.DIESEL,
        TipoA.EJECUTIVO, 5, 6, 250, True,
        TipoColor.NEGRO
    )

    auto1.imprimir()

    auto1.velocidad_actual = 100
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.acelerar(20)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(50)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.frenar()
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(20)
    print(f"Número de multas = {auto1.numero_multas()}")
    
    #Prueba multas
    auto1.velocidad_actual = 100
    print(f"Velocidad actual = {auto1.velocidad_actual}")
    
    auto1.acelerar(160)
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.acelerar(10) #Un incremento mas
    print(f"Velocidad actual = {auto1.velocidad_actual}")

    auto1.desacelerar(10) #No sube si desacelera pero sigue por encima de la vel. max.
    print(f"Número de multas = {auto1.numero_multas()}")

    print(f"Número de multas = {auto1.numero_multas()}")