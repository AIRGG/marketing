from flask import render_template, redirect, url_for, jsonify
import pandas as pd
import util.utility as utility
from util.koneksi import getCnnTag
from datetime import datetime

from flask import render_template, session
import datetime
import mainhttp

class ListenMsgGet:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def tampilLogin(self):
        return render_template('w_login.html', params="params")

    def tampilRegister(self):
        return render_template("w_register.html")

    def tampilBeranda(self):
        return render_template('w_beranda.html', params="params")

    def tampilUser(self, request):
        if not "u" in request.args:
            return "Upss.."
        ke = request.args["u"]
        param = {}
        if ke == "so":
            param["lvl"] = "SO"
            return render_template("user/u_so.html", params=param)
        if ke == "sm":
            param["lvl"] = "SM"
            return render_template("user/u_sm.html", params=param)
        if ke == "sh":
            param["lvl"] = "SH"
            return render_template("user/u_sh.html", params=param)
        if ke == "sa":
            param["lvl"] = "SA"
            return render_template("user/u_sa.html", params=param)

    def tampilProduk(self):
        return render_template("w_produk.html")

    def tampilJatuhTempo(self):
        return render_template("w_jatuhtempo.html")

    def tampilPengumuman(self):
        return render_template("w_pengumuman.html")

    def tampilLaporan(self):
        return render_template("w_laporan.html")
    # def tampilAktivasi(self):
    #     # data = ak(self.conn).getData()
    #     data = "asd"
    #     return render_template("w_aktivasi.html", data=data)

    def logout(self):
        return redirect('/'+mainhttp.dcontext+'/login')
            
        
    def getUserData(self):
        # data = ak(self.conn).getData()
        # return data.to_json(orient="records")
        return "Haii"
    