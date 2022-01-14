import base64
import json
import os
import pandas as pd
import ssl

from get_multas import get_multas_amazonia

import gspread
import requests
from flask import Flask, render_template

app = Flask(__name__)
spreadsheet_id = os.environ["SPREADSHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)
service_account = gspread.service_account_from_dict(credentials)
amazonia = ['AC', 'AM', 'AP','MA','PA','MT','RR','RO','TO']

@app.route("/")
def hello_world():
    arquivo = open("templates/home.html")
    return arquivo.read()

@app.route("/sobre")
def sobre():
    arquivo = open("templates/sobre.html")
    return arquivo.read()

@app.route("/multas")
def multas():
    arquivo = open("templates/multas.html")
    return arquivo.read()

@app.route("/ac")
def ac():
    arquivo = open("templates/multasac.html")
    return arquivo.read()

@app.route("/am")
def am():
    arquivo = open("templates/multasam.html")
    return arquivo.read()

@app.route("/ap")
def ap():
    arquivo = open("templates/multasap.html")
    return arquivo.read()

@app.route("/ma")
def ma():
    arquivo = open("templates/multasma.html")
    return arquivo.read()

@app.route("/mt")
def mt():
    arquivo = open("templates/multasmt.html")
    return arquivo.read()

@app.route("/pa")
def pa():
    arquivo = open("templates/multaspa.html")
    return arquivo.read()

@app.route("/ro")
def ro():
    arquivo = open("templates/multasro.html")
    return arquivo.read()

@app.route("/rr")
def rr():
    arquivo = open("templates/multasrr.html")
    return arquivo.read()

@app.route("/to")
def to():
    arquivo = open("templates/multasto.html")
    return arquivo.read()
