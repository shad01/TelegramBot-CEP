from telepot.loop import MessageLoop
from time import sleep
import telepot
import requests


def handle(msg):
	content_type, chat_type, chat_id = telepot.glance(msg)

	if content_type == "text":
		cep = msg['text']
		r = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
		r_json = r.json()

		consulta = f"""cep: {r_json['cep']}\nlogradouro: {r_json['logradouro']}
complemento: {r_json['complemento']}\nbairro: {r_json['bairro']}
localidade: {r_json['localidade']}\nuf: {r_json['uf']}\nunidade: {r_json['unidade']}
ibge: {r_json['ibge']}\ngia: {r_json['gia']}"""

		bot.sendMessage(chat_id, consulta) #Envia por usuário o resultado da consulta
		print(cep) #mostra as mensagens enviada para o bot

TOKEN = "" #Token do bot
bot = telepot.Bot(TOKEN) 

MessageLoop(bot, handle).run_as_thread()
print("Escutando...")

while 1:
	sleep(10)
