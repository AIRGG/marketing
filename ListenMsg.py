from flask import render_template, redirect, url_for
import pandas as pd
import util.utility as utility
from util.someprocess import Login as lg
from util.someprocess import Aktivasi as ak
from datetime import datetime

import mainhttp

from flask import session

class ListenMsgPost:
	def __init__(self, conn):
		self.conn = conn
		self.cursor = conn.cursor()

	def prosesLogin(self, request):
		print("haii")

	def prosesRegister(self, request):
		data = lg(self.conn).prosesRegister(request)
		if data == 1:
			return redirect("/"+mainhttp.dcontext+"/login?psn=success-register")
		else:
			return "Something Error"

	def getUserData(self, request):
		# print(request.json["kode"])
		data = ak(self.conn).getData(request)
		return data.to_json(orient="records")
	def changeStatusUser(self, request):
		data = ak(self.conn).changeStatusUser(request)
		return data

#Kita tambah suatu konten
def someFunction():
	return False