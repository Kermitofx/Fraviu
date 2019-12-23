#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import os, sys
import telebot
from telebot import types
from random import randint, choice

bot = telebot.TeleBot("833645402:AAE2k_0zF-VZhsb8D1tCBLWCLDnlZFrKnyk")

@bot.message_handler(commands=["paciencia", "paciencia@SrKingBot"])
def paciencia(message):
		list = [" paciência " ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "Minha *{}* Ta *{}*% Hoje💬".format(resposta, valor), parse_mode='Markdown')
		
		
		##Medo 
	
@bot.message_handler(commands=["medo", "medo@SrKingBot" ])
def medo(message):
		list = [" Medo" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "eu tô com *{}%* de  *{}* Hoje😕".format(valor, resposta), parse_mode='Markdown')
		
		
		##raiva
@bot.message_handler(commands=["raiva", "raiva@SrKingBot"])
def frase_command(message):
		list = [" Raiva" ]
		valor = randint(0, 100)
		resposta = choice(list)
		bot.reply_to(message, "Hoje eu tô com *{}%* De *{}* Hoje😠".format(valor, resposta), parse_mode='Markdown')
		
  	###start
@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, "Oie ✌\n\n Olha Meus Commands Disponíveis :) \n /paciencia = *Medidor De Paciência* 💬\n /medo = *Medidor de Medo* 😕 \n /raiva = *Medidor de Raiva😠* ")
		
		
  
bot.polling( )
