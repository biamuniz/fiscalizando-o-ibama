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
    return """
    <h1>Veja as multas em homologação/prazo de defesa em cada estado da Amazônia Legal</h1>
    <a href="/ac">Acre</a>
    <a href="/am">Amazonas</a>
    <a href="/ap">Amapá</a>
    <a href="/ma">Maranhão</a>
    <a href="/mt">Mato Grosso</a>
    <a href="/pa">Pará</a>
    <a href="/ro">Rondônia</a>
    <a href="/rr">Roraima</a>
    <a href="/to">Tocantins</a>
    """"


