import pandas as pd
import datetime, os
from flask import session

class Aktivasi:
	def __init__(self, conn):
		self.conn = conn
		self.cursor = conn.cursor()

	def crsr(self, sql, stmt=False):
		try:
			conNya = self.conn
			cursor = self.cursor
			if(stmt == False):
				cursor.execute(sql)
			else:
				cursor.execute(sql, stmt)
			conNya.commit()
		except Exception as e:
			print(e)
		return 1

	def getData(self, request):
		kode = request.json["kode"]
		if(kode == "0"):
			sql = "SELECT  * FROM user NATURAL JOIN karyawan WHERE lvl != 0"
			isi = pd.read_sql((sql), self.conn)
		else:
			sql = "SELECT  * FROM user NATURAL JOIN karyawan WHERE nip=%s AND lvl != 0"
			isi = pd.read_sql(sql, self.conn, params=[request.json["kode"]])
		return isi
	def changeStatusUser(self, request):
		kode = request.json["kode"]
		flg = request.json["to"]

		sql = "UPDATE user SET flag=%s WHERE username=%s"
		self.crsr(sql, (str(flg), str(kode)))
		return "oke"
		

class Login:
	"""docstring for Login"""
	def __init__(self, conn):
		self.conn = conn
		self.cursor = conn.cursor()

	def crsr(self, sql, stmt=False):
		try:
			conNya = self.conn
			cursor = self.cursor
			if(stmt == False):
				cursor.execute(sql)
			else:
				cursor.execute(sql, stmt)
			conNya.commit()
		except Exception as e:
			print(e)
		return 1

	def baca(self, sql):
		sql = pd.read_sql(sql, self.conn)
		return sql

	def prosesRegister(self, request):
		dt = request.form
		username = dt["username"]
		password = dt["password"]
		name = dt["name"]
		address = dt["address"]
		nip = dt["nip"]
		lvl = 2
		flag = 0
		sts = 1

		# sql = "INSERT INTO user VALUES('%s', '%s', '%s', '%s', '%s', '%s')" % (str(username),str(password),str(name),str(address),str(lvl),str(flag))
		sql = "INSERT INTO karyawan VALUES(%s, %s, %s, %s)"
		isi = self.crsr(sql, (str(nip),str(name),str(address),str(sts)))
		if isi == 1:
			sql1 = "INSERT INTO user VALUES(%s, %s, %s, %s, %s)"
			isi1 = self.crsr(sql1, (str(username),str(nip),str(password),str(lvl),str(flag)))
			return isi1
