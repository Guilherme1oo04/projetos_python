import math
import sys

txt_escolha_tipo_num = """
    1 - É um número inteiro ou flutuante
    2 - É uma fração
    3 - É uma raiz
    4 - É uma fração e raiz
    """

def equacao_geral():
    txt_c_angular = """
    Para prosseguir, informe sobre como deseja achar o coeficiente angular!

    1 - Eu já sei o coeficiente angular
    2 - Quero descobrir usando o ângulo de inclinação da reta
    3 - Quero descobrir usando dois pontos conhecidos

    Digite o número da sua escolha!
    """

    print(txt_c_angular)
    escolha_c_angular = input("Número: ")

    if escolha_c_angular == "1":
        print("Agora, iremos pegar o coeficiente angular, escolha uma opção para prosseguir!")
        print(txt_escolha_tipo_num)
        tipo_num = input("Tipo: ")

        if tipo_num == "1":
            c_angular = float(input("Coeficiente angular: "))
            print("Agora precisaremos de um ponto conhecido dessa reta!")
            ponto_da_reta = pontos_reta(1)

            equacao = f"Y - ({ponto_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * ponto_da_reta[0]['X']})"

            print(f"Essa é a equação geral dessa reta:")
            print(equacao)

        elif tipo_num == "2":
            print("Digite a fração nesse formato: 2/3")
            fracao = input("Fração: ")

            if fracao.find("/") == -1:
                print("Fração inválida!")
                sys.exit()
            else:
                fracao = eval(fracao)
                c_angular = float(fracao)

                print("Agora precisaremos de um ponto conhecido dessa reta!")
                ponto_da_reta = pontos_reta(1)

                equacao = f"Y - ({ponto_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * ponto_da_reta[0]['X']})"

                print(f"Essa é a equação geral dessa reta:")
                print(equacao)

        elif tipo_num == "3":
            print("Precisaremos saber o número a calcular e o tipo de raiz(Ex: raiz cúbica = 3)")
            tipo_raiz = float(input("Informe o tipo de raiz: "))
            num_raiz = float(input("Informe o número na raiz: "))

            raiz = num_raiz ** (1 / tipo_raiz)
            c_angular = raiz

            print("Agora precisaremos de um ponto conhecido dessa reta!")
            ponto_da_reta = pontos_reta(1)

            equacao = f"Y - ({ponto_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * ponto_da_reta[0]['X']})"

            print(f"Essa é a equação geral dessa reta:")
            print(equacao)

        elif tipo_num == "4":
            print("Primeirammente precisamos saber a raiz!")

            print(" ")
            print("Precisaremos saber o número a calcular e o tipo de raiz(Ex: raiz cúbica = 3)")
            tipo_raiz = float(input("Informe o tipo de raiz: "))
            num_raiz = float(input("Informe o número na raiz: "))

            raiz = num_raiz ** (1 / tipo_raiz)

            print(" ")
            print("Agora precisamos do número que está dividindo essa raiz")
            divide_raiz = float(input("Número que divide: "))

            num_final = raiz / divide_raiz
            c_angular = num_final

            print("Agora precisaremos de um ponto conhecido dessa reta!")
            ponto_da_reta = pontos_reta(1)

            equacao = f"Y - ({ponto_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * ponto_da_reta[0]['X']})"

            print(f"Essa é a equação geral dessa reta:")
            print(equacao)

        else:
            print("Resposta inválida!")

    elif escolha_c_angular == "2":
        print(" ")
        angulo = float(input("Digite o ângulo: "))
        rad = math.radians(angulo)
        c_angular = round(math.tan(rad))
        print("Agora precisaremos de um ponto conhecido dessa reta!")
        print(" ")
        ponto_da_reta = pontos_reta(1)

        equacao = f"Y - ({ponto_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * ponto_da_reta[0]['X']})"

        print(f"Essa é a equação geral dessa reta:")
        print(equacao)

    elif escolha_c_angular == "3":
        print("Precisaremos de dois pontos conhecidos da reta!")
        pontos_da_reta = pontos_reta(2)

        c_angular = (pontos_da_reta[1]['Y'] - pontos_da_reta[0]['Y']) / (pontos_da_reta[1]['X'] - pontos_da_reta[0]['X'])

        equacao = f"Y - ({pontos_da_reta[0]['Y']}) = {c_angular} * X - ({c_angular * pontos_da_reta[0]['X']})"

        print(f"Essa é a equação geral dessa reta:")
        print(equacao)

    else:
        print("Resposta inválida!")


def pontos_reta(num_pontos):
    pontos = []

    for x in range(0, num_pontos):
        ponto = {"X": 0, "Y": 0}
        coordenadas = ["X", "Y"]

        for c in coordenadas:
            print(f"Agora pegaremos o {c} do ponto {x + 1}!")

            print(txt_escolha_tipo_num)
            escolha_tipo = input("Tipo: ")

            if escolha_tipo == "1":
                numero = float(input("Informe o número: "))
                ponto[c] = numero

            elif escolha_tipo == "2":
                print("Digite a fração nesse formato: 2/3")
                fracao = input("Fração: ")

                if fracao.find("/") == -1:
                    print("Fração inválida!")
                    sys.exit()
                else:
                    fracao = eval(fracao)
                    ponto[c] = float(fracao)

            elif escolha_tipo == "3":
                print("Precisaremos saber o número a calcular e o tipo de raiz(Ex: raiz cúbica = 3)")
                tipo_raiz = float(input("Informe o tipo de raiz: "))
                num_raiz = float(input("Informe o número na raiz: "))

                raiz = num_raiz ** (1/tipo_raiz)
                ponto[c] = raiz

            elif escolha_tipo == "4":
                print("Primeirammente precisamos saber a raiz!")

                print(" ")
                print("Precisaremos saber o número a calcular e o tipo de raiz(Ex: raiz cúbica = 3)")
                tipo_raiz = float(input("Informe o tipo de raiz: "))
                num_raiz = float(input("Informe o número na raiz: "))

                raiz = num_raiz ** (1 / tipo_raiz)

                print(" ")
                print("Agora precisamos do número que está dividindo essa raiz")
                divide_raiz = float(input("Número que divide: "))

                num_final = raiz/divide_raiz
                ponto[c] = num_final

        pontos.append(ponto)
    return pontos