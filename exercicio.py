

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