import requests
import time
import json
import os


class TelegramBot:

  def __init__(self):
    token = "5675860672:AAHY6AEhAbvrqgh95WGWpGBWgqGN_Curdag"
    self.url_base = f"https://api.telegram.org/bot{token}/"

  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem, primeira_mensagem)
          self.responder(resposta, chat_id)

  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)

    return json.loads(resultado.content)

  def criar_resposta(self, mensagem, primeira_mensagem):
    mensagem = mensagem['message']['text']
    if primeira_mensagem == True or mensagem.lower() == "menu":
      return f'''Olá bem vindo a Va - Cursos{os.linesep}1 - Ajuda{os.linesep}2 - Cursos{os.linesep}3 - App'''
    if mensagem == "1":
      return "Como podemos te ajudar?"
    if mensagem == "2":
      return "Temos SQL"
    if mensagem == "3":
      return "Temos app para android"

    else:
      return "Digite menu para ver o menu"

  def responder(self, resposta, chat_id):
    link_envio = f"{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}"
    requests.get(link_envio)


bot = TelegramBot()
bot.Iniciar()
