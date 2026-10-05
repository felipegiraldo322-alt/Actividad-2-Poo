#Ejercicio 2.2. Definición de atributos de una clase con tipos primitivos de datos

from enum import Enum

class TipoPlaneta(Enum):

    GASEOSO = "GASEOSO"
    TERRESTRE = "TERRESTRE"
    ENANO = "ENANO"

class Planeta:

    def __init__(self, nombre, cantidad_satelites, masa, volumen, diametro, distancia_sol, tipo, es_observable, periodo_orbital=None, periodo_rotacional=None):
        
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa = masa
        self.volumen = volumen
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo = tipo
        self.es_observable = es_observable
        self.periodo_orbital = periodo_orbital
        self.periodo_rotacional = periodo_rotacional

    def imprimir(self):

        print(f"Nombre del planeta = {self.nombre}")
        print(f"Cantidad de satélites = {self.cantidad_satelites}")
        print(f"Masa del planeta = {self.masa}")
        print(f"Volumen del planeta = {self.volumen}")
        print(f"Diámetro del planeta = {self.diametro}")
        print(f"Distancia al sol = {self.distancia_sol}")
        print(f"Tipo de planeta = {self.tipo.name}")
        print(f"Es observable = {self.es_observable}")

    def calcular_densidad(self) -> float:

        return self.masa / self.volumen if self.volumen != 0 else 0

    def es_planeta_exterior(self) -> bool:

        limite = 508632758.0
        return self.distancia_sol > limite

    def calcular_periodo_orbital(self) -> float:

        return (self.distancia_sol ** 3) ** 0.5

    def calcular_periodo_rotacional(self) -> float:

        return ((self.distancia_sol ** 3) ** 0.5) * 365.25

p1 = Planeta("Tierra", 1, 5.972e24, 1.083e12, 12756, 1, TipoPlaneta.TERRESTRE, True)

p1.imprimir()
print(f"Densidad del planeta = {p1.calcular_densidad()}")
print(f"Es planeta exterior = {p1.es_planeta_exterior()}")
print(f"Período orbital del planeta en Años = {p1.calcular_periodo_orbital()}")
print(f"Período rotacional del planeta en Días = {p1.calcular_periodo_rotacional()}")

p2 = Planeta("Júpiter", 79, 1.898e27, 1.431e15, 142984, 5.2, TipoPlaneta.GASEOSO, True)

p2.imprimir()
print(f"Densidad del planeta = {p2.calcular_densidad()}")  
print(f"Es planeta exterior = {p2.es_planeta_exterior()}")
print(f"Período orbital del planeta en Años = {p2.calcular_periodo_orbital()}")
print(f"Período rotacional del planeta en Días = {p2.calcular_periodo_rotacional()}")