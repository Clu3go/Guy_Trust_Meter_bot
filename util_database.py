#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

class DataBase():

	def __init__(self, dbname=""):
		self.dbname = dbname
		self.conn = sqlite3.connect(dbname)
		self.c = self.conn.cursor()
		return

	def check_user_id(self, user_id):
		args = (str(user_id),)
		stmt = self.c.execute("SELECT CASE WHEN EXISTS (SELECT * FROM '' WHERE user_id=(?)) THEN CAST (1 AS BIT) ELSE CAST(0 AS BIT) END", args)
		flag = stmt.fetchone()[0]
		return flag

	def add_feedback(self, feedback_text):
		args = (feedback_text,)
		self.c.execute("INSERT INTO 'Feedbacks' ('Messages') VALUES ((?))", args)
		self.conn.commit()
		

	def check_access_flag(self, user_id):
		args = (user_id,)
		stmt = self.c.execute("SELECT IFNULL(, 0) FROM '' WHERE user_id=(?)", args)
		return stmt.fetchone()[0]

	def add_access_flag(self, user_id):
		args = (user_id,)
		self.c.execute("UPDATE '' SET '' = 1 WHERE user_id=(?)", args)
		self.conn.commit()
		return
