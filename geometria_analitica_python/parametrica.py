import matplotlib.pyplot as plt

def parametrica():
    print("Para começar, informe as equações paramétricas!")
    print("Escreva nesse formato: 2t - 5")
    x = input("X = ")
    y = input("Y = ")

    termos_x = x.split()

    if termos_x[0].find("t") != -1:
        num_t = float(termos_x[0].replace("t", ""))

        num_solto = float(termos_x[2]) * (-1)

        t = ''

        if num_solto < 0:
            t = f"(X/{num_t} - ({float(termos_x[2])}))"

        elif num_solto > 0:
            t = f"(X/{num_t} + ({float(termos_x[2])}))"

        else:
            t = f"(X/{num_t})"

        print(f"t = {t}")

        new_t = "*" + t

        y = y.replace("t", new_t)

        print(f"Y = {y}")

        valores_x = [-1, 0, 1]
        valores_y = []

        for x in valores_x:
            valor_x = str(x)
            y1 = y.replace("X", valor_x)
            valor_y = eval(y1)
            valores_y.append(valor_y)

        fig, ax = plt.subplots()

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        ax.plot(valores_x, valores_y)

        ax.set_title('Gráfico de equação paramétrica')
        ax.set_xlabel('Eixo x')
        ax.set_ylabel('Eixo y')

        plt.show()


    elif termos_x[2].find("t") != -1:
        num_t = termos_x[0].replace("t", "")
        num_t = termos_x[1] + num_t
        num_t = float(num_t)

        num_solto = float(termos_x[0]) * (-1)

        t = ''

        if num_solto < 0:
            t = f"(X/{num_t} - ({float(termos_x[0])}))"

        elif num_solto > 0:
            t = f"(X/{num_t} + ({float(termos_x[0])}))"

        else:
            t = f"(X/{num_t})"

        print(f"t = {t}")

        new_t = "*" + t

        y = y.replace("t", new_t)

        print(f"Y = {y}")

        valores_x = [-1, 0, 1]
        valores_y = []

        for x in valores_x:
            valor_x = str(x)
            y1 = y.replace("X", valor_x)
            valor_y = eval(y1)
            valores_y.append(valor_y)

        fig, ax = plt.subplots()

        ax.axhline(y=0, color='k')
        ax.axvline(x=0, color='k')

        ax.plot(valores_x, valores_y)

        ax.set_title('Gráfico de equação paramétrica')
        ax.set_xlabel('Eixo x')
        ax.set_ylabel('Eixo y')

        plt.show()
