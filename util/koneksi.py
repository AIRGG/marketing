# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 23:40:44 2019

@author: adrns
"""
import pyodbc
import pymysql

class getCnnTag:
    def __init__(self, cn, dbtuser, dbtpass, dbtname, dbtserver, dbtclass):
        self.conn = cn
        self.dbuser = dbtuser
        self.dbpass = dbtpass
        self.dbserver = dbtserver
        self.dbclass = dbtclass
        self.dbname = dbtname

    def getConn(self):
       
        conn = pyodbc.connect('DRIVER={'+ self.dbclass +'};'
                          'SERVER='+self.dbserver+';'
                          'DATABASE='+self.dbname+';'
                          'UID='+self.dbuser+';'
                          'PWD='+self.dbpass+'')
        return conn

    def getConnMysql(self):
        conn = None
        # splitport = self.dbserver.split(":")
        # ip = splitport[0]
        # port = splitport[1]
        print(self.dbpass)
        if self.dbpass != None and self.dbpass != '':
            conn = pymysql.connect(host = self.dbserver, user = self.dbuser, password = self.dbpass, database = self.dbname,  charset="utf8")
        else:
            conn = pymysql.connect(host = self.dbserver, user = self.dbuser, password = '', database = self.dbname,  charset="utf8")
        return conn
    
def getClassDB():
    listDriver = ['SQL Server', 'MySQL Driver']
    return listDriver