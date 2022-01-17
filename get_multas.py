import base64
import json
import os
import pandas as pd
import ssl
import gspread
import requests

ssl._create_default_https_context = ssl._create_unverified_context
spreadsheet_id = os.environ["SPREADSHEET_ID"]
conteudo_codificado = os.environ["GOOGLE_SHEETS_CREDENTIALS"]
conteudo = base64.b64decode(conteudo_codificado)
credentials = json.loads(conteudo)
service_account = gspread.service_account_from_dict(credentials)


amazonia = ['AC', 'AM', 'AP','MA','PA','MT','RR','RO','TO']
for UF in amazonia:
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

planilha = spreadsheet.worksheet(Amazonia)
AC = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/AC/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
AM = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/AM/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
AP = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/AP/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
MA = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/MA/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
MT = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/MT/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
PA = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/PA/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
RO = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/RO/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
RR = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/RR/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
TO = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/TO/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
aml = pd.concat([AC, AM, AP, MA, MT, PA, RO, RR, TO], ignore_index=True)
aml = aml.loc[aml['Situação Débito'] == 'Para homologação/prazo de defesa']
aml = aml.loc[aml['Tipo Auto'] == 'Multa']
del aml['Nº AI']
del aml['Data Auto']
del aml['Enquadramento Legal']
dadosaml = aml.groupby(['UF', 'Município', 'Tipo Infração', 'Última Atualização Relatório']).size().to_frame(name = 'count').reset_index().sort_values(by=['count'],ascending=False)
planilha.update([dadosaml.columns.values.tolist()] + dadosaml.values.tolist())
