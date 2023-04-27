from equacaoGeral import pontos_reta

def distanciaPontos():
    txt_inicial = "Iremos calcular a distância entre dois pontos!"

    print(txt_inicial)
    pontos = pontos_reta(2)

    a = pontos[1]['X'] - pontos[0]['X']
    b = pontos[1]['Y'] - pontos[0]['Y']
    d = ((a ** 2) + (b ** 2)) ** (1/2)

    print(f"A distância entre ({pontos[0]['X']}, {pontos[0]['Y']}) e ({pontos[1]['X']}, {pontos[1]['Y']}) é igual a: {d}")

