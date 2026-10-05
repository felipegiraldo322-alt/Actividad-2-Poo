#Ejercicio 2.5. Definición de métodos con parámetros

from enum import Enum

class TipoCuenta(Enum):
    AHORROS = 1
    CORRIENTE = 2

class CuentaBancaria:

    def __init__(self, nombresTitular, apellidosTitular, numeroCuenta, tipoCuenta, interesMensual):
        self.nombresTitular = nombresTitular
        self.apellidosTitular = apellidosTitular
        self.numeroCuenta = numeroCuenta
        self.tipoCuenta = tipoCuenta
        self.interesMensual = interesMensual
        self.saldo = 0

    def imprimir(self):
        print("Nombres del titular =", self.nombresTitular)
        print("Apellidos del titular =", self.apellidosTitular)
        print("Número de cuenta =", self.numeroCuenta)
        print("Tipo de cuenta =", self.tipoCuenta.name)
        print("Interés mensual =", self.interesMensual, "%")
        print("Saldo =", self.saldo)

    def consultarSaldo(self):
        print("El saldo actual es =", self.saldo)

    def consignar(self, valor):

        if valor > 0:
            self.saldo = self.saldo + valor

            print("Ha consignado $", valor, "en la cuenta. El nuevo saldo es $", self.saldo)

            return True

        else:
            print("El valor a consignar debe ser mayor que cero.")
            return False

    def retirar(self, valor):

        if valor > 0 and valor <= self.saldo:
            self.saldo = self.saldo - valor

            print("Ha retirado $", valor, "de la cuenta. El nuevo saldo es $",self.saldo)

            return True

        else:
            print("El valor a retirar debe ser menor que el saldo actual.")
            return False

    def calcularInteres(self):

        interes = self.saldo * self.interesMensual / 100
        self.saldo = self.saldo + interes

        print("Se ha aplicado un interés de $", interes, ". El nuevo saldo es $" ,self.saldo)

cuenta = CuentaBancaria("Pedro", "Pérez", 123456789, TipoCuenta.AHORROS, 2)

cuenta.imprimir()

cuenta.consignar(200000)

cuenta.consignar(300000)

cuenta.retirar(400000)

cuenta.calcularInteres()

cuenta.consultarSaldo()