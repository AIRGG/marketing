# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 22:23:24 2019

@author: adrns
"""


from xml.dom import minidom

dbUser = 'admin'
dbPassword = ''
dbUrl = 'localhost'
dbName = 'dbdb'
dbClass = 'dbClass'
dbtUser = 'admin'
dbtPassword = 'admin'
dbtUrl = 'localhost'
dbtClass = '{SQL SERVER}'
regid = 'test'
dbregister = 'kosong'
dbKeyApi = ''
ucontext = 'uload'
dcontext = 'dload'
hardwareid = ''
versiApp = '05.build.1121'
port = 5002
allowip = ''
prodak = ''

def loadXml():
    global dbUser, dbregister, dbPassword, dbUrl, dbClass
    global dbtUser, dbtPassword, dbtUrl, dbtClass
    global ucontext, dcontext, hardwareid, versiApp
    global port, dbName, regid, allowip, prodak

    eElement = minidom.parse('confighttp.xml')

    # nList = doc.getElementsByTagName(doc.firstChild.tagName)
    # for node1 in doc.getElementsByTagName("dbClass"):
    #     for node2 in node1.childNodes:
    #         print(node2.data)

    if getTagValue("dbUser", eElement) != '':
        dbUser = getTagValue('dbUser', eElement)

    if getTagValue("dbPassword", eElement) != (""):
        dbPassword = getTagValue("dbPassword", eElement)

    if getTagValue("dbUrl", eElement) != (""):
        dbUrl = getTagValue("dbUrl", eElement)

    if getTagValue("dbClass", eElement) != (""):
        dbClass = getTagValue("dbClass", eElement)

    if getTagValue("dbUser", eElement) != (""):
        dbUser = getTagValue("dbUser", eElement)

    if getTagValue("dbPassword", eElement) != (""):
        dbPassword = getTagValue("dbPassword", eElement)

    if getTagValue("dbUrl", eElement) != (""):
        dbUrl = getTagValue("dbUrl", eElement)

    if getTagValue("dbtClass", eElement) != (""):
        dbtClass = getTagValue("dbtClass", eElement)

    if getTagValue("portbuka", eElement) != (""):
        port = int(getTagValue("portbuka", eElement))

    if getTagValue("regid", eElement) != (""):
        regid = getTagValue("regid", eElement)

    if getTagValue("ucontext", eElement) != (""):
        ucontext = getTagValue("ucontext", eElement)

    if getTagValue("dcontext", eElement) != (""):
        dcontext = getTagValue("dcontext", eElement)

    if getTagValue("verdev", eElement) != (""):
        versiApp = getTagValue("verdev", eElement)
    
    if getTagValue("dbName", eElement) != (""):
        dbName = getTagValue("dbName", eElement)
    
    if getTagValue("allowip", eElement) != (""):
        allowip = getTagValue("allowip", eElement)

    if getTagValue("prd", eElement) != (""):
        prodak = getTagValue("prd", eElement)

def getTagValue(sTag, element):
    x = ''
    for nodes in element.getElementsByTagName(sTag):
        node = nodes.childNodes
        if(len(node) > 0):
            x = node[0].data
    return x