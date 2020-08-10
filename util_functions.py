#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# bunch of lists globally required
languages = ['eng', 'Eng', 'English', 'english', 'ita', 'Ita', 'italiano', 'Italiano']
languages_ita = ['ita', 'Ita', 'italiano', 'Italiano']
languages_eng = ['eng', 'Eng', 'English', 'english']


info_about_dic = {"Ita": "Guy_trust_meter nasce come strumento d'aiuto per contrastare il fenomeno del revenge porn su Telegram. Dal momento che Telegram \
					non sembra interessato ad agire attivamente per contrastare e bloccare gruppi nati con lo scopo di permettere a persone di scambiarsi anonimante \
					contenuti pornografici (e pedopornografici), gli utenti sono lasciati in balia di se stessi. \nGli strumenti classici come la segnalazione dei gruppi\
					non è né sufficiente né efficacie, dal momento che questi gruppi possono essere ricreati nel giro di pochi giorni.\
					È per questo che abbiamo deciso di crare un database di utenti che fanno o hanno fatto parte di questi gruppi, per permettere a chiunque sia\
					interessato di controllare se un contatto fa parte di questo database. \nÈ importante sottolineare che un match positivo con un contatto \
					significa solamente che il contatto faceva parte di uno dei gruppi durante la creazione del database o durante uno degli aggiornamenti. \
					Questo significa che un contatto POTREBBE NON ESSERE PIU' PARTE DI QUEI GRUPPI, ma abbiamo scelto di mantenere nel database anche i contatti \
					di utenti che si sono tolti dai gruppi dopo la creazione della prima versione del database. \n \
					Un'altra nota importante è che il bot NON CONSENTE ALTRE AZIONI se non quella di controllare i propri contatti. \n \
					Siamo disposti a fornire il database alle autorità competenti ma non è possibile tramite il bot segnalare persone o altro. \n \
					Lo scopo del bot rimane solamente quello di dare uno strumento in più alle persone per inquadrare meglio amici, potenziali partner, figli e altre categorie \
					per cui l'appartenenza ai gruppi di revenge porn rappresenta un campanello d'allarme. \n \
					Ribadiamo ancora che un match positivo NON SIGNIFICA che il contatto in questione abbia diffuso o scaricato materiale dai gruppi, ma SOLAMENTE che ne ha fatto parte.",

				"Eng": "Guy_trust_meter is meant as a tool to help counter the revenge porn phenomenon on Telegram. Since Telegram \
					does not seem interested in taking active actions to oppose and block groups born with the aim of allowing people to exchange in anonymity \
					pornographic (and pedopornographic) content, users are left alone. \n Classic tools such as group reporting\
					is neither sufficient nor effective, since these groups can be recreated within a few days.\
					That's why we decided to create a database of users who are or have been part of these groups, to allow anyone who's \
					interested to check if one of its contacts is part of this database. \It's important to stress that a positive match with a contact is NOTHING MORE than a positive match. \
					This only means that the contact was part of one of the groups during the creation of the database or during one of its updates. \
					This implies also that a contact COULD BE NOT ANYMORE PART OF THOSE GROUPS, but we have chosen to keep the contacts in the database as well \
					of users who have removed themselves from the groups after creating the first version of the database. \n \
					Another important note is that the bot DOES NOT allow any other action other than checking your own contacts. \n \
					We are willing to provide the database to the competent authorities but it is not possible through the bot to report people or anything else. \n \
					The purpose of the bot remains only to give people an extra tool to better judge friends, potential partners, one's own children and other categories \
					for which the belonging to revenge porn groups should be a wake-up call. \n \
					We want to stress again that a positive match DOES NOT MEAN that the contact in question has send or downloaded material from the groups, but ONLY that it joined one of them."}


info_feedback_dic = {"Ita" : "Puoi inviarci feedbacks o consigli su come migliorare il bot digitando Feed: prima del testo del messaggio. \nNon superare i 300 caratteri (50 parole in media). \nQuesto limite è necessario per evitare spam e per permetterci di leggere tutti i messaggi agevolmente.",
					"Eng" : "You can send us feedbacks or suggentions to improve the bot by typing Feed: before the message's text. \nDon't type more than 300 characters (50 words on average). \nThis limit is necessary to avoid spam and to allow us to easily read all the messages."}


info_contacts_dic = {"Ita" : "Puoi contattarci tramite email: guytrustmeterbot@gmail.com \nIl codice del bot (senza database) è visionabile al link:  ",
					"Eng" : "You can contact us trough email: guytrustmeterbot@gmail.com \nThe code (without database) can be checked at this link: "}



def reply_commands(message, language):
	if (message == "/start") or (message == "/language"):
		reply = select_language()

	elif message == "/about":
		reply = info_about(language)

	elif message == "/feedback":
		reply = info_feedback(language)

	else:
		reply = info_contacts(language)

	return reply



def info_about(language):
	if language in languages_ita:
		reply = info_about_dic["Ita"]
	else:
		reply = info_about_dic["Eng"]
	return reply 



def info_feedback(language):
	if language in languages_ita:
		reply = info_feedback_dic["Ita"]
	else:
		reply = info_feedback_dic["Eng"]
	return reply



def info_contacts(language):
	if language in languages_ita:
		reply = info_contacts_dic["Ita"]
	else:
		reply = info_contacts_dic["Eng"]
	return reply



def select_language():
	reply = "Type Eng for English o digita Ita per Italiano."
	return reply




def greetings(language):
	if language in languages_ita:
		reply = "Benvenut*! Questo bot è stato creato con lo scopo di permetterti di controllare se uno dei tuoi contatti fa o ha \
		fatto parte di uno dei gruppi di revenge porn di telegram. \nPer farlo è sufficente inviare il contatto della persona che vuoi controllare\
		su questa chat clikkando la clip 📎 in basso a destra. \nIl controllo è basato su ricerche esterne degli utenti appartenenti a questi gruppi svolte periodicamente dagli\
		sviluppatori del bot. Questo significa che anche se il bot restituisce un no come risposta, il contatto potrebbe comunque\
		far parte di un gruppo che non è ancora stato controllato dagli svilupattori. \nPer iniziare, invia semplicemente un contatto."

	else:
		reply = "Welcome! This bot was created to allow you to check if one of your contacts belongs to or has joined one of the telegram's\
		revenge porn gropus. \nTo do so just send a contact you would like to check to this conversation by clicking the paperclip 📎 below, at the bottom right. \nThe control is based on an external\
		research of users belonging to these grops made by the developers of the bot. \nThis implies that even if the bot provides a no answer, it might\
		be the case that the contact is anyway part of a group that has not been checked by the developers yet. \nTo start, just send a contact."

	return reply



def reply_check_user(check, language):
	if check and (language in languages_eng):
		reply = "⚠️ Pay attention! Your contact has been found in our database."
	elif check and (language in languages_ita):
		reply = "⚠️ Fa attenzione! Il tuo contatto è presente nel nostro database."
	elif not check and (language in languages_eng):
		reply = "Your contact has not been found in any of the group present in our database."
	else:
		reply = "Il tuo contatto non è stato trovato in nessun gruppo presente nel nostro database."
	return reply



def reply_error_contact(language):
	if language in languages_ita:
		reply = "Controlla che il tuo contatto abbia un account telegram. \n(puoi controllare cercando il nome con cui è salvato in rubrica nella barra di ricerca di telegram)."
	else:
		reply = "Please check that your concat has a telegram account. \n(you can check by searching the name you saved in your contacts in the telegram search bar)."
	return reply



def reply_error_message(language):
	if language in languages_ita:
		reply = "Per favore, invia un contatto, o digita /start per selezionare nuovamente la lingua. \nAltre azioni per ora non sono disponibili"
	else:
		reply = "Please send a contact, or type /start to select again the language. \nOther actions are not available yet."
	return reply



def reply_error_feedback(language):
	if language in languages_ita:
		reply = "Non puoi inviare feedbacks più lunghi di 300 caratteri."
	else:
		reply = "You can't send feedbacks longer than 300 characters."
	return reply



def reply_thanks_feedback(language):
	if language in languages_ita:
		reply = "Grazie per il feedback!"
	else:
		reply = "Thanks for your feedback!"
	return reply