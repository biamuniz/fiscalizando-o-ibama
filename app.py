import pandas as pd
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
def get_multas():  
    df = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/RR/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
    df = df.loc[df['Situação Débito'] == 'Para homologação/prazo de defesa']
    df = df.loc[df['Tipo Auto'] == 'Multa']
    # deletando colunas que não são necessárias na visualização
    del df['Nº AI']
    del df['Data Auto']
    del df['Enquadramento Legal']
    dados = df.groupby(['Município', 'Tipo Infração', 'Última Atualização Relatório']).size().to_frame(name = 'count').reset_index().sort_values(by=['count'],ascending=False)
    return """<h1>Multas na Amazônia Legal</h1>"""
    df
    
    
@app.route("/teste")
def get_multas_amazonia_legal():  
    return """
        <h1>Multas na Amazônia Legal</h1>
        <p>
            <div class="flourish-embed flourish-chart" data-src="visualisation/8391891"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
        </p>
            """
