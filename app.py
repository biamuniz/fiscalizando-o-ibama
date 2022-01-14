import base64
import json
import os
import pandas as pd
import ssl

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

def get_multas():
    ssl._create_default_https_context = ssl._create_unverified_context
    UF = input("Digite a sigla da unidade de federação: ")
    UF = UF.upper()
    if UF in amazonia:
      url = "https://dadosabertos.ibama.gov.br/dados/SICAFI/"+UF+"/Quantidade/multasDistribuidasBensTutelados.csv"
      df = pd.read_csv(url, sep=';')
      spreadsheet = service_account.open_by_key(spreadsheet_id)
      worksheet = spreadsheet.worksheet(UF)
      df = df.loc[df['Situação Débito'] == 'Para homologação/prazo de defesa']
      df = df.loc[df['Tipo Auto'] == 'Multa']
      del df['Nº AI']
      del df['Data Auto']
      del df['Enquadramento Legal']
      dados = df.groupby(['Município', 'Tipo Infração', 'Última Atualização Relatório']).size().to_frame(name = 'count').reset_index().sort_values(by=['count'],ascending=False)
      worksheet.update([dados.columns.values.tolist()] + dados.values.tolist())
    else:
      print("Esta UF não pertence ao território da Amazônia Legal!")
    return UF

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
    UF = get_multas()
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

