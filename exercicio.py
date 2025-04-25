
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

