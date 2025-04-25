import math


def calculo_lampada():

    largura = float(input("digite a largura: "))
    comprimento = float(input("digite o comprimento: "))

    metro_quadrado = largura * comprimento

    potencia_lampada = int(input("qual a pontencia da lampada? "))

    print("lampadas necessarias: ", math.ceil((metro_quadrado*3)/potencia_lampada))

calculo_lampada()