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
