#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
import aiml
from telebot import types
from random import randint, choice


kernel = aiml.Kernel()
kernel.bootstrap(learnFiles="startup.xml", commands="LOAD AIML BOT")

bot = telebot.TeleBot("833645402:AAHEPKnaDVd2YpJWsgg14GI9JH-ydRoqh08")

is_silenced = False


@bot.message_handler(commands=["off"])
def handle_start(m):
    global is_silenced
    is_silenced = True
    bot.reply_to(m, "*Conversa em chat silênciada*:(\n\n _PORQUE VOCE FEZ ISSO? DXA EU CONVERSA COM MEUS AMIGOS_ /unoff")


@bot.message_handler(commands=["unoff"])
def handle_start(m):
    global is_silenced
    is_silenced = False
    bot.reply_to(m, "Saúde! Eu posso conversar!")


###paciência 

@bot.message_handler(commands=["/paciencia"])
def paciencia(m):
	if m.text == '/paciencia' or m.text == '/paciencia@SrKingBot ' or m.text == 'paciência' :
		list = ["😑 | Paciência" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "Minha*{}* tá *{}*% Hoje✨".format(resposta, valor), parse_mode='Markdown')
		
		
		##Medo 
	
@bot.message_handler(commands=["/medo"])
def medo(m):
	if m.text == '/medo' or m.text == '/medo@SrKingBot ' or m.text == 'medo' :
		list = ["😕 | Medo" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "eu to*{}%* de  *{}*Hoje✨".format(valor, resposta), parse_mode='Markdown')
		
		
		##raiva
@bot.message_handler(commands=["/raiva"])
def frase_command(m):
	if m.text == '/raiva' or m.text == '/raiva@SrKingBot ' or m.text == 'raiva' :
		list = ["😠 | Raiva" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(m, "Hoje Eu Tô *{}%* De *{}* Hoje✨".format(valor, resposta), parse_mode='Markdown')
		
  	###start
  
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.reply_to(chat_id, "Oie\n\n Olha Meus Commands Disponíveis :) ✌\n `/Paciência` = `*Medidor De Paciência* 😑 \n `/medo` = *Medidor de Medo* 😢 \n `/raiva` = *Medidor de Raiva* 😠")
  
  
  ##resposta aiml
@bot.message_handler(func=lambda message: True, content_types=["text"])
def response(m):
    global is_silenced
    if message.text == "silence_all" or message.text == "SILENCE_ALL":
        is_silenced = True
    if message.text == "unsilence_all" or message.text == "UNSILENCE_ALL":
        is_silenced = False
        return
    if is_silenced:
        return
    response_text = kernel.respond(message.text, message.chat.id)
    bot.reply_to(m, response_text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
