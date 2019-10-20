import os
from flask import Flask, render_template, request, redirect, url_for, session

import numpy.random.common
import numpy.random.bounded_integers
import numpy.random.entropy

import mainhttp
from ListenMsg import ListenMsgPost as listenPost
from ListenMsgGet import ListenMsgGet as listenGet
from flask_restful import Resource, Api
from util.koneksi import getCnnTag
from datetime import datetime, timedelta
import pyodbc
import sys
import uuid
#coba lagii
mainhttp.loadXml()
app = Flask(__name__)
app.secret_key = 'B12Loc2391038OOOOMG'
# app.config["CACHE_TYPE"] = "null"
api = Api(app)
app.permanent_session_lifetime = timedelta(minutes=5)
check = False

user = 'IBAALTON'
pw = 'BID4LT0ND3VELOPmEnT'

def main():
	cnn = None
	
	try:
		cnn = getCnnTag(cnn, mainhttp.dbUser, mainhttp.dbPassword,
					mainhttp.dbName, mainhttp.dbUrl, mainhttp.dbClass).getConnMysql()
	except Exception as ex:
		print('Database Not Connect ',ex)
		wait()
		return

	try:
		cnn.close()
	except Exception as ex:
		pass

	startServer()

def startServer():
	print('URL Pattern: /'+mainhttp.dcontext+'')
	print('Register Code: '+ str(hex(uuid.getnode())))
	app.run(host="0.0.0.0", port=mainhttp.port, debug=True, threaded=True)

@app.context_processor
def getDateTime():
	return {"now":datetime.utcnow()}

@app.route('/'+mainhttp.dcontext+'/<string:path>',  methods=['GET'])
def getMapping(path):
	rtr = ''
	cnn = None
	cnn = getCnnTag(cnn, mainhttp.dbUser, mainhttp.dbPassword,mainhttp.dbName, mainhttp.dbUrl, mainhttp.dbClass).getConnMysql()
	lt = listenGet(cnn)
#aa
	if path == 'login':
		rtr = lt.tampilLogin()
	if path == 'register':
		rtr = lt.tampilRegister()

	if path == 'beranda':
		rtr = lt.tampilBeranda()
	if path == 'user':
		rtr = lt.tampilUser(request)
	if path == 'produk':
		rtr = lt.tampilProduk()
	if path == 'jatuhtempo':
		rtr = lt.tampilJatuhTempo()
	if path == 'pengumuman':
		rtr = lt.tampilPengumuman()
	if path == 'laporan':
		rtr = lt.tampilLaporan()

	if path == 'logout':
		rtr = lt.logout()

	return rtr

@app.route('/'+mainhttp.dcontext+'/<string:path>',  methods=['POST'])
def routeMainServer(path):
	rtr = None
	cnn = None

	if request.method == 'POST':        
		cnn = getCnnTag(cnn, mainhttp.dbUser, mainhttp.dbPassword,
						mainhttp.dbName, mainhttp.dbUrl, mainhttp.dbClass)

		conn = cnn.getConnMysql()

		lt = listenPost(conn)
		
		if path == 'login':
			rtr = lt.prosesLogin(request)
		if path == 'register':
			rtr = lt.prosesRegister(request)

		return rtr


@app.route('/'+mainhttp.dcontext, methods=['GET'])
def getDefaultMapping():
	return redirect('/'+mainhttp.dcontext+'/login')

import msvcrt as m
def wait():
	m.getch()

if __name__ == '__main__':
	main()