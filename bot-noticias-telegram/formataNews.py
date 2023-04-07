from buscaNews import buscaNoticias

def formata(tituloMsg, tema):
    texto = [f"""{tituloMsg}\n"""]

    noticias = buscaNoticias(tema)

    for x in noticias:
        noticia = f"""{x['title']}\n \nData: {x['date']}\n {x['desc']}\n \nLink da notícia: {x['link']}\n \n"""
        texto.append(noticia)

    return texto