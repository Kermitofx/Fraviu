#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
import aiml
from telebot import types
from random import randint, choice


bot = telebot.TeleBot("833645402:AAE2k_0zF-VZhsb8D1tCBLWCLDnlZFrKnyk")

###paciência 

@bot.message_handler(commands=["/paciencia"])
def paciencia(m):
	if m.text == '/paciencia' or m.text == '/paciencia@SrKingBot ' or m.text == 'paciência' :
		list = ["😑 | Paciência" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to_message_id(m, "Minha*{}* tá *{}*% Hoje✨".format(resposta, valor), parse_mode='Markdown')
		
		
		##Medo 
	
@bot.message_handler(commands=["/medo"])
def medo(m):
	if m.text == '/medo' or m.text == '/medo@SrKingBot ' or m.text == 'medo' :
		list = ["😕 | Medo" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to_message_id(m, "eu to*{}%* de  *{}*Hoje✨".format(valor, resposta), parse_mode='Markdown')
		
		
		##raiva
@bot.message_handler(commands=["/raiva"])
def frase_command(m):
	if m.text == '/raiva' or m.text == '/raiva@SrKingBot ' or m.text == 'raiva' :
		list = ["😠 | Raiva" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to_message_id(m, "Hoje Eu Tô *{}%* De *{}* Hoje✨".format(valor, resposta), parse_mode='Markdown')
		
  	###start
  
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.reply_to_message_id(chat_id, "Oie\n\n Olha Meus Commands Disponíveis :) ✌\n `/Paciência` - `*Medidor De Paciência* 😑 \n `/medo` - *Medidor de Medo* 😢 \n `/raiva` - *Medidor de Raiva* 😠")
  
  
  ##resposta aiml

if __name__ == '__main__':
    bot.polling(none_stop=True)
