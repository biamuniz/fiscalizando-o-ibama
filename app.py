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
    UF = get_multas_amazonia()
    if UF = "AC":
        arquivo = open("templates/multasac.html")
    elif UF = "AM":
        arquivo = open("templates/multasam.html")
    elif UF = "AP":
        arquivo = open("templates/multasap.html")
    elif UF = "MA":
        arquivo = open("templates/multasma.html")
    elif UF = "MT":
        arquivo = open("templates/multasmt.html")
    elif UF = "PA":
        arquivo = open("templates/multaspa.html")
    elif UF = "RO":
        arquivo = open("templates/multasro.html")
    elif UF = "RR":
        arquivo = open("templates/multasrr.html")
    elif UF = "TO":
        arquivo = open("templates/multasto.html")
    else:
        arquivo = open("templates/erro.html")
    return arquivo.read()

