import glob
import os.path
from tkinter import *
from tkinter.filedialog import askopenfilename
from moviepy.editor import *
from pytube import YouTube

class App:

    def __init__(self):

        # variáveis que são necessárias serem criadas antes

        self.arquivo = ''

        self.janela = Tk()
        self.janela.title('Audio downloader')
        self.janela.minsize(600, 300)

        self.inicio = Label(
            text='Escolha uma das opções para prosseguir',
            font=('Helvetica', 15)
        )
        self.inicio.pack(padx=10, pady=10)

        self.opcoes = Frame(self.janela)

        self.radio_valor = IntVar()
        self.radio_valor.set(1)

        self.opcao1 = Radiobutton(
            self.opcoes,
            text='Vídeo baixado',
            font=('Helvetica', 15),
            variable= self.radio_valor,
            value=1
        )
        self.opcao2 = Radiobutton(
            self.opcoes,
            text='Vídeo do Youtube',
            font=('Helvetica', 15),
            variable=self.radio_valor,
            value=2
        )

        self.opcao1.grid(row=0, column=0)
        self.opcao2.grid(row=0, column=1)

        self.opcoes.pack()

        self.audio_opcoes()

        mainloop()

    def audio_opcoes(self):
        self.valor = self.radio_valor.get()

        if (self.valor == 1):

            self.opcao1.configure(command='')
            self.opcao2.configure(command=self.audio_opcoes)

            self.opcao1.configure(value=3)

            self.escolher = Button(
                text='Escolha o vídeo:',
                font=('Helvetica', 15),
                command=self.abreArquivo
            )
            self.escolher.pack(pady=15)

            self.caminho = Entry(
                font=('Helvetica', 15),
                state='disabled'
            )
            self.caminho.pack(padx=15, pady=5, fill='both', ipadx=5)

            self.extrair = Button(
                text='Extrair aúdio',
                font=('Helvetica', 15),
                command=self.extrair_baixado
            )
            self.extrair.pack(ipadx=5, ipady=5, pady=5)

        elif (self.valor == 2):

            self.escolher.destroy()
            self.caminho.destroy()
            self.extrair.destroy()

            self.opcao2.configure(command='')
            self.opcao1.configure(command=self.audio_opcoes)

            self.insira_link = Label(
                text='Insira o link do vídeo abaixo',
                font=('Helvetica', 15)
            )
            self.insira_link.pack(pady=15)

            self.link = Entry(
                font=('Helvetica', 15)
            )
            self.link.pack(padx=15, pady=5, fill='both', ipadx=5)

            self.bt_extrair_link = Button(
                text='Extrair aúdio',
                font=('Helvetica', 15),
                command=self.extrair_youtube
            )
            self.bt_extrair_link.pack(ipadx=5, ipady=5, pady=5)

        elif (self.valor == 3):

            self.insira_link.destroy()
            self.link.destroy()
            self.bt_extrair_link.destroy()

            self.opcao1.configure(command='')
            self.opcao2.configure(command=self.audio_opcoes)

            self.opcao1.configure(value=3)

            self.escolher = Button(
                text='Escolha o vídeo:',
                font=('Helvetica', 15),
                command=self.abreArquivo
            )
            self.escolher.pack(pady=15)

            self.caminho = Entry(
                font=('Helvetica', 15),
                state='disabled'
            )
            self.caminho.pack(padx=15, pady=5, fill='both', ipadx=5)

            self.extrair = Button(
                text='Extrair aúdio',
                font=('Helvetica', 15),
                command=self.extrair_baixado
            )
            self.extrair.pack(ipadx=5, ipady=5, pady=5)

    def abreArquivo(self):
        self.arquivo = askopenfilename()
        self.caminho.configure(state='normal')
        self.caminho.delete(0, 'end')
        self.caminho.insert(0, self.arquivo)
        self.caminho.configure(state='disabled')

    def extrair_baixado(self):
        self.texto_do_caminho = self.caminho.get()

        if (self.texto_do_caminho != ''):

            if (self.texto_do_caminho == 'Primeiro escolha um vídeo!'):
                self.caminho.configure(state='normal')
                self.caminho.delete(0, 'end')
                self.caminho.insert(0, 'Primeiro escolha um vídeo!')
                self.caminho.configure(state='disabled')

            elif (self.texto_do_caminho == 'Extração Concluída'):
                self.caminho.configure(state='normal')
                self.caminho.delete(0, 'end')
                self.caminho.insert(0, 'Primeiro escolha um vídeo!')
                self.caminho.configure(state='disabled')

            else:
                mp4 = VideoFileClip(self.texto_do_caminho)
                dividir_nome = self.texto_do_caminho.split('/')
                nome_arquivo = dividir_nome[-1]
                nome_mp3 = f'{nome_arquivo[:-4]}.mp3'
                mp4.audio.write_audiofile(os.path.join(nome_mp3))

                self.caminho.configure(state='normal')
                self.caminho.delete(0, 'end')
                self.caminho.insert(0, 'Extração Concluída')
                self.caminho.configure(state='disabled')

        else:
            self.caminho.configure(state='normal')
            self.caminho.delete(0, 'end')
            self.caminho.insert(0, 'Primeiro escolha um vídeo!')
            self.caminho.configure(state='disabled')

    def extrair_youtube(self):
        self.texto_link = self.link.get()

        if (self.texto_link == ''):
            self.link.insert(0, 'Primeiro insira um link aqui!')

        elif (self.texto_link == 'Primeiro insira um link aqui!'):
            self.link.delete(0, 'end')
            self.link.insert(0, 'Primeiro insira um link aqui!')

        else:
            yt = YouTube(self.texto_link)
            yd = yt.streams.get_highest_resolution()
            yd.download()
            lista_mp4 = glob.glob('*.mp4')
            nome_video = lista_mp4[0]

            mp4_yt = VideoFileClip(os.path.join(nome_video))
            nome_mp3_yt = f'{nome_video[:-4]}.mp3'
            mp4_yt.audio.write_audiofile(os.path.join(nome_mp3_yt))
            mp4_yt.close()

            os.remove(nome_video)


App()

