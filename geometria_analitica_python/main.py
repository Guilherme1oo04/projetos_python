from equacaoGeral import equacao_geral
from equacaoSegm import equaSegmentada
from distanciaDoisPontos import distanciaPontos
from parametrica import parametrica

txt_inicial = """
Olá, para prosseguir, escolha uma das seguintes escolhas!

1 - Distância entre dois pontos
2 - Equação geral da reta
3 - Equação segmentada da reta
4 - Equação paramétrica da reta

Digite o número da sua escolha!"""
print(txt_inicial)
escolha_inicial = input("Escolha: ")

if escolha_inicial == "1":
    distanciaPontos()
elif escolha_inicial == "2":
    equacao_geral()
elif escolha_inicial == "3":
    equaSegmentada()
elif escolha_inicial == "4":
    parametrica()
else:
    print("Execução finalizada por preenchimento inválido!")
