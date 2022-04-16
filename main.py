# Importar o App, Builder (GUI)
## Criar nosso App
## Criar a função Build
import requests
from kivy.app import App
from kivy.lang import Builder

GUI = Builder.load_file("tela.kv")

class MeuAplicativo(App):
    def build(self):
        return GUI

    def on_start(self):
        # Colocar chamada da Câmera aqui passando o valor para o label de texto abaixo:
        self.root.ids["texto1"].text = f"Dólar: {self.pegar_cotacao('USD')}"
        self.root.ids["texto2"].text = f"Euro: {self.pegar_cotacao('EUR')}"
        self.root.ids["texto3"].text = f"Bitcoin: {self.pegar_cotacao('BTC')}"
        self.root.ids["texto4"].text = f"Ethereum: {self.pegar_cotacao('ETH')}"

    def pegar_cotacao(self, moeda):
        link = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
        requisicao = requests.get(link)
        print(requisicao.json())
        dic_requisicao = requisicao.json()
        cotacao = dic_requisicao[f"{moeda}"]["bid"]
        return cotacao

MeuAplicativo().run()