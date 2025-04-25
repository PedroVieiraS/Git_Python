import math

def calculo_lampada():

    largura = float(input("digite a largura: "))
    comprimento = float(input("digite o comprimento: "))

    metro_quadrado = largura * comprimento

    potencia_lampada = int(input("qual a pontencia da lampada? "))

    print("lampadas necessarias: ", math.ceil((metro_quadrado*3)/potencia_lampada))

def calcular_azulejos():
    comprimento = float(input(""))
    largura = float(input(""))
    altura = float(input(""))

    total = comprimento*largura*altura

    print("quantidade de azulejos e de: ", total, math.ceil(total/1.5))



def calculo_combustivel():
    combustivel = 4.87
    odometro_inicial = float(input("digite o odometro inicial: \n"))
    odometro_final = float(input("digite o odometro final: \n"))
    combustivel_gasto = float(input(""))
    valor_recebido = float(input(""))

    total_percorrido = odometro_final - odometro_inicial

    gasto_gasolina = combustivel_gasto * combustivel

    media_consumo_kml = total_percorrido / combustivel_gasto

    lucro = valor_recebido - gasto_gasolina

    print("media consumo ", media_consumo_kml)
    print("gasto com gasolina", gasto_gasolina)
    print("lucro ", lucro)


def regiao():

    resposta = int(input("digite a regiao "))

    match resposta:
        case 1:
            print("Sul")
        case 2:
            print("Norte")
        case 3:
            print("Leste")
        case 4:
            print("Oeste")
        case 5:
            print("Nordeste")
        case 6:
            print("Nordeste")
        case 7:
            print("Sudeste")
        case 8:
            print("Sudeste")
        case 9:
            print("Sudeste")
        case 10:
            print("Centro-Oeste")
        case 11:
            print("Noroeste")
        case _:
            print("Importado")

def media():
    nota1 = float(input("digite sua primeira nota"))
    nota2 = float(input("digite sua segunda nota"))

    nota_media = (nota1+nota2)/2

    match nota_media:
        case x if x >= 6:
            print("Aprovado")
        case x if x < 3:
            print("Reprovado")
        case x if x >= 3 and x < 6:
            op = int(input("voce fez a avaliação optativa? sim-1/nao-0"))
            match op:
                case x if x == 1:
                    notaoptativa = float(input("Qual foi sua nota na avaliação optativa? "))
                    
                    notamenor = nota2 if nota1 > nota2 else nota1
                    notamaior = nota2 if nota1 < nota2 else nota1


                    if notaoptativa > notamenor:
                        notamenor = notaoptativa
                    
                    mediafinal = (notamaior+notamenor)/2

                    print("media final", mediafinal)
                     

                case x if x == 0:
                    notaoptativa = -1

                    print("sua media sem optativa", nota_media)







