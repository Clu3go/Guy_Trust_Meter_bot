#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests 
import json
import configparser as cfg
import urllib.parse

class telegram_chatbot():

	def __init__(self):
		#self.config = self.open_config_file()
		self.token = self.read_token_from_config_file()
		self.base = "https://api.telegram.org/bot{}".format(self.token)
		self.url = self.base + "/getUpdates?timeout=100"
		self.r = requests.get(self.url) 
		self.keyboard = json.dumps({'keyboard': [["/feedback", "/language"],["/about", "/contacts"]], 'resize_keyboard': True})


	def read_token_from_config_file(self):
		parser = cfg.RawConfigParser()
		config_path = r"./config.cfg"
		parser.read(config_path)
		return parser.get("creds", "token")


	def get_updates(self, offset=None):
		if offset:
			url = self.url + "&offset={}".format(offset + 1)
		else:
			url = self.base
		r_new = requests.get(url)
		return json.loads(r_new.content)


	def send_message(self, msg, chat_id):
		params = {"chat_id": str(chat_id), "text": msg, "reply_markup": self.keyboard}
		query = urllib.parse.urlencode(params)
		url_send = self.base + "/SendMessage?" + query
		if msg is not None:
			requests.get(url_send)
