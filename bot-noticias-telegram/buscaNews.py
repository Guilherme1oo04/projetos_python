from GoogleNews import GoogleNews
import requests
import json

def buscaNoticias(tema):
    google_news = GoogleNews(period='d')
    google_news.set_lang('pt-br')
    google_news.search(tema)

    resultado = google_news.result()

    openai_key = "chave_api_openai"
    header_require = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/completions"
    id_modelo = "text-davinci-003"

    noticias_resumidas = []
    for x in resultado:
        body_message = {
            "model": id_modelo,
            "prompt": f"Faça um resumo de no máximo 5 linhas dessa notícia: {x['link']}",
            "temperature": 0.5,
            "max_tokens": 200
        }
        body_message = json.dumps(body_message)

        requisicao = requests.post(link, headers=header_require, data=body_message)

        resposta = requisicao.json()

        resumo = resposta["choices"][0]["text"]

        noticias_resumidas.append(resumo)

    for y in range(0, len(noticias_resumidas)):
        resultado[y]['desc'] = noticias_resumidas[y]

    return resultado
