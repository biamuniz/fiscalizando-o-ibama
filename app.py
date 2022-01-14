from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <h1>Fiscalizando o Ibama</h1>
        <a href="/sobre">Sobre esse site</a>
        <p>
            Visualizando a quantidade de multas ambientais aplicadas no âmbito do Ibama que estão em <b>homologação ou prazo de defesa</b> nos estados que integram o território da Amazônia Legal.
        </p>
    """

@app.route("/sobre")
def sobre():
    return """
        <h1>Sobre</h1>
        <a href="/">Página inicial</a>
        <p>
            Esse site foi criado por <b>Bianca Muniz</b> como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do Insper.
        </p>
            """

@app.route("/amazonia")
def get_multas_amazonia_legal():  
    UF = input("Digite a sigla da unidade de federação: ")
    UF = UF.upper()
    if UF in amazonia:
      url = "https://dadosabertos.ibama.gov.br/dados/SICAFI/"+UF+"/Quantidade/multasDistribuidasBensTutelados.csv"
      df = pd.read_csv(url, sep=';')
      spreadsheet = service_account.open_by_key(spreadsheet_id) # "abrir" o arquivo
      worksheet = spreadsheet.worksheet(UF) # escolhe uma aba
      df = df.loc[df['Situação Débito'] == 'Para homologação/prazo de defesa']
      df = df.loc[df['Tipo Auto'] == 'Multa']
      # deletando colunas que não são necessárias na visualização
      del df['Nº AI']
      del df['Data Auto']
      del df['Enquadramento Legal']
      dados = df.groupby(['Município', 'Tipo Infração', 'Última Atualização Relatório']).size().to_frame(name = 'count').reset_index().sort_values(by=['count'],ascending=False)
      worksheet.update([dados.columns.values.tolist()] + dados.values.tolist())
    else:
      print("Esta UF não pertence ao território da Amazônia Legal!")
    return UF
            """
