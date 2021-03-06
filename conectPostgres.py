#! /usr/bin/env python
# -*- coding: utf-8 -*-

import psycopg2

class Database:   
    def __init__(self):
		try:
			
			self.connection = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='12345'")
			self.cursor = self.connection.cursor()
			print "Conectado"
		except:
			print "I am unable to connect to the database"
		
		

    def query(self,q,data_param,typequery):
		self.typequery=typequery
		cursor = self.cursor
		self.data_param=data_param
		if self.typequery=='S':
			#S: Select SQL 
			print q, self.typequery,self.data_param
			if self.data_param=='':
				cursor.execute(q)
			else:
			    cursor.execute(q,data_param)
			rows=cursor.fetchall()
			return rows
		elif self.typequery=='SL':	
			#SL: SQL Select for like 
			dato = (data_param,)
			#print q,dato
			cursor.execute(q,dato)
			rows=cursor.fetchall()
			return rows
		elif self.typequery=='U':
			#U: update operation SQL
			cursor.execute(q,data_param)
			self.connection.commit()			
		elif self.typequery=='I':
			#I: insert operation SQL
			cursor.execute(q,data_param)
			self.connection.commit()
			return True	
		elif self.typequery=='D':
			#D: Delete operation SQL
			cursor.execute(q,data_param)
			self.connection.commit()
		elif self.typequery=='II':
			#I: insert image operation SQL
			idd=data_param[0]
			img=data_param[1]
			binario = sqlite3.Binary(img)
			data_paramx=(idd,binario)
			print data_paramx
			cursor.execute(q,data_paramx)
			self.connection.commit()			
						
    def __del__(self):
        self.connection.close()
