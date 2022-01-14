from flask import Flask, request
import pandas as pd

app = Flask(__name__)

def dados_multas():
    df = pd.read_csv("https://dadosabertos.ibama.gov.br/dados/SICAFI/RR/Quantidade/multasDistribuidasBensTutelados.csv", sep=';')
    df = df.loc[df['Situação Débito'] == 'Para homologação/prazo de defesa']
    df = df.loc[df['Tipo Auto'] == 'Multa']
    del df['Nº AI']
    del df['Data Auto']
    del df['Enquadramento Legal']
    dados = df.groupby(['Município', 'Tipo Infração', 'Última Atualização Relatório']).size().to_frame(name = 'count').reset_index().sort_values(by=['count'],ascending=False)
    return dados
 

@app.route("/")
def hello_world():
    return """
        <h1>Fiscalizando o Ibama</h1>
        <a href="/teste">Testes</a> - <a href="/sobre">Sobre esse site</a>
        <p>
            Visualizando a quantidade de multas ambientais aplicadas no âmbito do Ibama que estão em <b>homologação ou prazo de defesa</b> nos estados que integram o território da Amazônia Legal.
        </p>
    """

@app.route('/multas', methods = ['POST', 'GET']) 
def multas(): 
   if request.method == 'POST': 
    UF = request.form['UF']  
      return
    """<body> 
    <form action = "UF" method = "POST">
        <p>Estado <input type = "text" name = "UF" /></p> 
         <p><input type = "submit" value = "submit" /></p> 
      </form>        
   </body>"""

@app.route("/sobre")
def sobre():
    return """
        <h1>Sobre</h1>
        <a href="/teste">Testes</a> - <a href="/">Página inicial</a>
        <p>
            Esse site foi criado por <b>Bianca Muniz</b> como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do Insper.
        </p>
            """

@app.route("/teste")
def teste():
    return """
        <h1>Teste</h1>
        <a href="/sobre">Sobre esse site</a> - <a href="/">Página inicial</a>
        <p>
            Teste de visualização
        </p>
        <div class="flourish-embed flourish-chart" data-src="visualisation/8391891"><script src="https://public.flourish.studio/resources/embed.js"></script></div>
            """

@app.route("/dados")
def dados_multas():
    dados = dados_multas()
    return f"""
    <h1>Multas no Pará</h1> 
    <a href="/sobre">Sobre esse site</a>
    <p> Dados
        {dados}
    </p>"""

