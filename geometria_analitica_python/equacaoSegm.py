def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)


def mmc(a, b):
    return abs(a * b) / mdc(a, b)


def equaSegmentada():
    txt_inicial = """
    Primeiramente informe o que deseja fazer!

    1 - Converter da segmentada para equação geral
    2 - Converter da geral para segmentada
    """
    print(txt_inicial)
    escolha = input("Escolha: ")

    if escolha == "1":
        print("Digite a equação nesse formato: x/5 + y/3 = 1")
        equacao = input("Equação: ")

        equacao_dividida = equacao.split()

        a = equacao_dividida[0].split("/")
        a = float(a[1])

        b = equacao_dividida[2].split("/")
        b = float(b[1])

        mmcAB = mmc(a, b)

        numX = mmcAB / a

        numY = mmcAB / b

        c = mmcAB

        equacao = f"{numX}X + {numY}Y - {c} = 0"

        print(f"Equação: {equacao}")

    elif escolha == "2":
        print("Digite a equação nesse formato: 1x + 6y - 10 = 0")
        equacao = input("Equação: ").lower()

        equacao_dividida = equacao.split()

        numX = float(equacao_dividida[0].replace("x", ""))
        numY = float(equacao_dividida[2].replace("y", ""))

        if equacao_dividida[3] == "-":
            c = float(equacao_dividida[4])
        elif equacao_dividida[3] == "+":
            c = float(equacao_dividida[4]) * (-1)

        a = c / numX
        b = c / numY

        equacao = f"X/{a} + Y/{b} = 1"

        print(f"Equação: {equacao}")
