#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

class DataBase():

	def __init__(self, dbname="Groups_members.db"):
		self.dbname = dbname
		self.conn = sqlite3.connect(dbname)
		self.c = self.conn.cursor()
		return


	def check_user_id(self, user_id):
		args = (user_id,)
		stmt = self.c.execute("SELECT CASE WHEN EXISTS (SELECT * FROM 'La_Bibbia_4.0' WHERE user_id=(?)) THEN CAST (1 AS BIT) ELSE CAST(0 AS BIT) END", args)
		flag = stmt.fetchone()[0]
		return flag


	def check_user_first_name(self, first_name):
		args = (first_name,)
		stmt = self.c.execute("SELECT COUNT(*) FROM 'La_Bibbia_4.0' WHERE firstname=(?)", args)
		flag = stmt.fetchone()[0]
		return flag


	def check_user_last_name(self, last_name):
		args = (last_name,)
		stmt = self.c.execute("SELECT COUNT(*) FROM 'La_Bibbia_4.0' WHERE lastname=(?)", args)
		flag = stmt.fetchone()[0]
		return flag


	def add_feedback(self, feedback_text):
		args = (feedback_text,)
		self.c.execute("INSERT INTO 'Feedbacks' ('Messages') VALUES ((?))", args)
		self.conn.commit()
		

	def check_access_flag(self, user_id):
		args = (user_id,)
		stmt = self.c.execute("SELECT IFNULL(access_temptative, 0) FROM 'La_Bibbia_4.0' WHERE user_id=(?)", args)
		return stmt.fetchone()[0]


	def add_access_flag(self, user_id):
		args = (user_id,)
		self.c.execute("UPDATE 'La_Bibbia_4.0' SET 'access_temptative' = 1 WHERE user_id=(?)", args)
		self.conn.commit()
		return
