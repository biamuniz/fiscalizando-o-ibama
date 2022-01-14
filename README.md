# **Fiscalizando o Ibama**
## **Atualização e visualização gráfica diária da quantidade de multas ambientais nos estados da Amazônia Legal**

Este repositório armazena os dados, códigos e outras informações sobre projeto **Fiscalizando o Ibama**, apresentado como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do master em Jornalismo de Dados, Automação e Data Storytelling do Insper. O projeto foi realizado sob orientação do professor [Eduardo Cuducos](https://github.com/cuducos) e utiliza conhecimentos desenvolvidos ao longo do semestre de formação.

## Sobre a proposta
Tendo em vista o [desmonte sofrido pelo Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis (Ibama)](https://extra.globo.com/noticias/um-so-planeta/desmonte-ambiental-ibama-so-tem-26-do-contingente-necessario-para-fiscalizacao-de-biomas-25109010.html) e a urgência em se preocupar com o território da Amazônia legal (que sofre com as ameaças do [garimpo ilegal](https://noticias.uol.com.br/ultimas-noticias/agencia-estado/2021/12/20/pf-encontra-alto-indice-de-mercurio-no-rio-madeira.htm) e do [desmatamento](https://www.bbc.com/portuguese/brasil-59341478)), este projeto pretende facilitar o acompanhamento de multas aplicadas nos estados da região com o status "para homologação/prazo de defesa" que não apresentam pagamento nas bases de dados do Ibama.

## Metodologia
Com a biblioteca `pandas` foi feita a leitura e análise das planilhas de multas ambientias por bens tutelados, disponíveis no [Portal de Dados Abertos do Ibama](https://dadosabertos.ibama.gov.br/). A biblioteca `ssl` também foi usada, para lidar com o certificado de segurança do site.
 
Foram utilizados os dados dos nove estados da Amazônia Legal: para cada UF, o código `get_multas.py` faz a leitura da planilha, filtra apenas as multas com o status para "homologação/prazo de defesa" e conta a quantidade de ocorrências por município. Ele ainda utiliza a biblioteca `gspread`, que preenche uma [planilha no Google Spreadsheets](https://docs.google.com/spreadsheets/d/1By5WRZLxlWEvh7I37tX1RUrh3XvA8FqWqC5gg_-ZiB0/edit?usp=sharing) toda vez que o código é rodado (tarefa programada no Heroku, a ser executada a cada dez minutos). A url da planilha está linkada à ferramenta Flourish, que a cada cinco minutos verifica se há alguma atualização dos dados no Google Sheets, atualizando também a visualização. **IMPORTANTE**: O Ibama atualiza diariamente o relatório de multas ambientais aplicadas; logo, não se espera grandes modificações entre solicitações realizadas em períodos mais curtos.

---------------------------------------------------------------------------------------------------

### Próximos passos
- [ ] Acrescentar o valor, em reais, que as multas representam;
- [ ] Adicionar outros status relevantes para acompanhamentos das multas (no projeto, foquei apenas em multas para homologação/prazo de defesa, mas há mais situações que podem ser analisadas).

### Dúvidas, críticas, comentários, sugestões?
Você pode me contatar por DM no [twitter](twitter.com/biancamuniz__), ou ainda, contribuir com este projeto!
#### Como contribuir:
* Faça o fork do [projeto](https://github.com/biamuniz/multas-amazonia-legal/), crie uma *branch* (ramificação) para a sua modificação, faça o *comitt* e submeta um *pull request*;
* Você também pode abrir uma *issue* com a sua sugestão ou comentário.
