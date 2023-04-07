import requests
import json

def resumirNews(linkNews):
    openai_key = "chave_api_openai"
    header_require = {"Authorization": f"Bearer {openai_key}", "Content-Type": "application/json"}
    link = "https://api.openai.com/v1/completions"
    id_modelo = "text-davinci-003"

    body_message = {
        "model": id_modelo,
        "prompt": f"Faça um resumo de no mínimo 100 palavras dessa notícia: {linkNews}",
        "temperature": 0.5,
        "max_tokens": 200
    }
    body_message = json.dumps(body_message)

    requisicao = requests.post(link, headers=header_require, data=body_message)

    resposta = requisicao.json()

    resumo = resposta["choices"][0]["text"]

    textoResumo = f"Resumo da notícia: {linkNews}\n {resumo}"

    return textoResumo
