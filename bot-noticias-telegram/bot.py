import telebot
from formataNews import formata
from verificaFatos import verifica
from resumeNews import resumirNews

chave_api = "Chave_api_telegram"

news = telebot.TeleBot(token=chave_api)

@news.message_handler(commands=['start'])
def start(message):
    texto = """
Oi! Eu sou um bot de notícias!

Esses são alguns dos comandos que eu posso executar:

/NoticiasImportantes 
Mostra as 10 notícias mais importantes do dia.
Para executar esse comando, basta clicar nele ou digitar e enviar no chat.

/Noticia 
Mostra 10 notícias sobre o tópico que você colocar.
Para executar ele, você pode clicar e esperar as instruções ou simplesmente digitar o comando e o tópico que quer saber no chat.
Exemplo: /Noticia Política

/ResumeNoticia
Esse comando resume a notícia de um link que você queira saber em específico.
Para executá-lo, basta clicar nele e esperar as instruções ou então escrever esse comando seguido do link a verificar.
Exemplo: /ResumeNoticia linkAqui 

/VerificaNoticia
Esse comando mostra se uma notícia é verdadeira ou falsa.
Para executá-lo, basta clicar e esperar as instruções
Para o comando funcionar, a notícia deve conter pelo menos 100 palavras, se não a análise não funciona corretamente e nem será exibida.
    """
    news.reply_to(message, texto)

@news.message_handler(commands=['Noticia'])
def noticia(message):
    texts = message.text.split()

    if len(texts) < 2:
        news.reply_to(message, "Digite sobre o que quer pesquisar!")
        news.register_next_step_handler(message, aguardar_tema)

    elif len(texts) > 2:
        news.reply_to(message, "Passe apenas um parâmetro!")

    else:
        news.reply_to(message, "Aguarde, pode demorar um pouco para carregar")
        tituloMsgTema = f"Notícias sobre o tema: {texts[1]}"
        mensagemsTema = formata(tituloMsgTema, texts[1])
        for x in mensagemsTema:
            mensagemTema = x
            news.reply_to(message, mensagemTema)

def aguardar_tema(message):
    texts = message.text.split()

    if len(texts) < 2:
        news.reply_to(message, "Aguarde, pode demorar um pouco para carregar")
        tituloMsgTema = f"Notícias sobre o tema: {texts[0]}"
        mensagemsTema = formata(tituloMsgTema, texts[0])
        for x in mensagemsTema:
            mensagemTema = x
            news.reply_to(message, mensagemTema)

    else:
        news.reply_to(message, "Passe apenas um parâmetro!")

@news.message_handler(commands=['NoticiasImportantes'])
def noticiasImportantes(message):
    news.reply_to(message, "Aguarde, pode demorar um pouco para carregar")
    tituloMsgTema = f"Notícias importantes do dia"
    mensagemsTema = formata(tituloMsgTema, "Noticias importantes")
    for x in mensagemsTema:
        mensagemTema = x
        news.reply_to(message, mensagemTema)

@news.message_handler(commands=['ResumeNoticia'])
def resumeNoticias(message):
    texts = message.text.split()

    if len(texts) < 2:
        news.reply_to(message, "Cole o link da notícia abaixo!")
        news.register_next_step_handler(message, aguardar_link)

    elif len(texts) > 2:
        news.reply_to(message, "Passe apenas um link!")
    else:
        news.reply_to(message, "Aguarde, pode demorar um pouco para carregar")
        noticiaResumida = resumirNews(texts[1])
        news.reply_to(message, noticiaResumida)

def aguardar_link(message):
    texts = message.text.split()

    if len(texts) < 2:
        news.reply_to(message, "Aguarde, pode demorar um pouco para carregar")
        noticiaResumida = resumirNews(texts[0])
        news.reply_to(message, noticiaResumida)

    else:
        news.reply_to(message, "Passe apenas um link!")

@news.message_handler(commands=['VerificaNoticia'])
def verificaNoticias(message):
    news.reply_to(message, "Digite a notícia completa abaixo, só funcionará caso possua pelo menos 100 palavras!")
    news.register_next_step_handler(message, aguardar_noticia)

def aguardar_noticia(message):
    text = message.text
    texts = message.text.split()

    if len(texts) < 100:
        news.reply_to(message, "Não é possível verificar, texto é muito pequeno!")

    else:
        classificacao = verifica(text)
        news.reply_to(message, classificacao)


news.polling()
