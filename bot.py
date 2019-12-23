#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("833645402:AAE2k_0zF-VZhsb8D1tCBLWCLDnlZFrKnyk")

@bot.message_handler(commands=["/paciencia"])
def paciencia(message):
	if m.text == '/paciencia@SrKingBot ' or m.text == 'paciÃªncia' :
		list = ["ðŸ˜‘ | PaciÃªncia" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "Minha*{}* tÃ¡ *{}*% Hojeâœ¨".format(resposta, valor), parse_mode='Markdown')
		
		
		##Medo 
	
@bot.message_handler(commands=["/medo"])
def medo(message):
	if m.text == '/medo' or m.text == '/medo@SrKingBot ' or m.text == 'medo' :
		list = ["ðŸ˜• | Medo" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "eu to*{}%* de  *{}*Hojeâœ¨".format(valor, resposta), parse_mode='Markdown')
		
		
		##raiva
@bot.message_handler(commands=["/raiva"])
def frase_command(message):
	if m.text == '/raiva' or m.text == '/raiva@SrKingBot ' or m.text == 'raiva' :
		list = ["ðŸ˜  | Raiva" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "Hoje Eu TÃ´ *{}%* De *{}* Hojeâœ¨".format(valor, resposta), parse_mode='Markdown')
		
  	###start
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
		
		
  
bot.polling( )
