#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from bot import telegram_chatbot
from util_database import DataBase
import util_functions as ut

update_id = 1

chat_bot = telegram_chatbot()

database = DataBase()

languages = ["eng", "Eng", "English", "english", "ita", "Ita", "italiano", "Italiano"]
commands = ["/contacts", "/feedback", "/language", "/about", "/start"]
default_language = "ita"

while True:

	updates = chat_bot.get_updates(offset=update_id)
	#print(updates) #print just to test purposes
	try:
		updates = updates["result"]
	except:
		# print message for developers
		print("Could not connect to the server.")

	if updates:
		for item in updates:
			
			from_ = item["message"]["from"]["id"]

			try:
				update_id = item["update_id"]
			except:
				print(type(item["update_id"]))
				print(item)

			# check if user seding request is in the database, if so update access_flag and start ignoring messages
			if bool(database.check_user_id(from_)):
				if bool(database.check_access_flag(from_)):
					reply = "You can't use this bot."
				else:
					database.add_access_flag(from_)

			# check if there are text messages
			else:
				try:
					message = item["message"]["text"]

					# first check if the user want to set the language cause default_language variable is required by all other functions 
					if message in languages:
						default_language = message
						reply = ut.greetings(default_language)

					# then check if the user is trying to use a command 
					elif message in commands:
						reply = ut.reply_commands(message, default_language)

					elif message[0:5] in ["Feed:", "feed:"]:
						if len(message[6:]) <= 300:
							database.add_feedback(message)
							reply = ut.reply_thanks_feedback(default_language)
						else:
							reply = ut.reply_error_feedback(default_language)

					# any other text is ignored
					else:
						reply = ut.reply_error_message(default_language)

				except:
					# if the message does not contain text we assume the user is sending a contact to check
					try:
						message = item['message']['contact']['user_id']
						#print(item['message']['contact'])
						check_flag = database.check_user_id(message)
						reply = ut.reply_check_user(check_flag, default_language)

					# if no user_id is found, we check if the user has set a first and a last name to use them as keys for the qwery
					except:
						try:
							first_name = item['message']['contact']['first_name']
							if first_name == '':
								first_name = None
							else:
								# check how many rows contains this first_name  
								first_name_flag = database.check_user_first_name(first_name)

						except:
							first_name = None
						try:
							last_name = item['message']['contact']['last_name']
							if last_name == '':
								last_name = None
							else:
								# same check as for last_name
								last_name_flag = database.check_user_last_name(last_name)
						except:
							last_name = None

						# if there's a match for first_name or last_name reply with info about the amount of correspondances found
						if (first_name is not None) or (last_name is not None):
							# dictionry to pass to the reply function both flags as a single argument 
							flags_dict = {}

							if first_name is not None:
								flags_dict['first_name'] = first_name_flag
							if last_name is not None:
								flags_dict['last_name'] = last_name_flag

							reply = ut.reply_check_user_name(flags_dict, first_name, last_name, default_language)

						else:
							reply = ut.reply_error_contact(default_language)

			chat_bot.send_message(reply, from_)

