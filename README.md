# **Multas ambientais na Amazônia Legal**

Este repositório armazena os dados, códigos e outras informações sobre projeto **Multas ambientais na Amazônia Legal**, apresentado como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do master em Jornalismo de Dados, Automação e Data Storytelling do Insper. O projeto foi realizado sob orientação do professor [Eduardo Cuducos](https://github.com/cuducos) e utiliza conhecimentos desenvolvidos ao longo do semestre de formação.

## Sobre a proposta
A aplicação de multas ambientais é uma ferramenta para frear atitudes ilegais contra o meio ambiente e diminuir a impunidade daqueles que cometem essas práticas. Acompanhar a aplicação e o status dessas multas pode ser uma boa fonte de investigações, visto que a quantidade e evolução dos status dessas multas dão pistas sobre o funcionamento do órgão de fiscalização em uma região. Por exemplo, o aumento de multas aplicadas pode indicar uma ação rigorosa de fiscalização; por outro lado, o aumento de multas aplicadas e que ainda não foram pagas pode sugerir atraso, negligência, falta de funcionários para fiscalizar, entre outras hipóteses.

Tendo em vista o desmonte sofrido pelo órgão e a urgência em se preocupar com o território da Amazônia legal, este projeto pretende facilitar o acompanhamento de multas aplicadas nos estados da região com o status "para homologação/prazo de defesa" que não apresentam pagamento nas bases de dados do Ibama.

## Metodologia
Fiz a leitura das planilhas de multas ambientais por bens tutelados, disponíveis no Portal de Dados Abertos do Ibama(), e análise usando a biblioteca `pandas`. Para a atualização automática da [planilha](https://docs.google.com/spreadsheets/d/1By5WRZLxlWEvh7I37tX1RUrh3XvA8FqWqC5gg_-ZiB0/edit?usp=sharing), foi utilizado o código descrito no [notebook](link). Nesta tarefa, utilizei a biblioteca `gspread`.

Para as visualizações de dados, foi utilizada a ferramenta Flourish com dados importados automaticamente da planilha disponibilizada no Google Sheets. A cada cinco minutos, a ferramenta atualiza, obtendo os dados mais novos da planilha. **IMPORTANTE**: O Ibama atualiza diariamente o relatório de multas ambientais aplicadas; logo, não se espera grandes modificações entre solicitações realizadas em períodos mais curtos.

---------------------------------------------------------------------------------------------------

### Perspectivas futuras
- [ ] Acrescentar o valor, em reais, que as multas representam;
- [ ] Adicionar outros status relevantes para acompanhamentos das multas (no projeto, foquei apenas em multas para homologação/prazo de defesa, mas há mais situações que podem ser analisadas).

### Dúvidas, críticas, comentários, sugestões?
Você pode me contatar por DM no [twitter](twitter.com/biancamuniz__), ou ainda, contribuir com este projeto!
#### Como contribuir:
* Faça o fork do [projeto](https://github.com/biamuniz/multas-amazonia-legal/), crie uma *branch* (ramificação) para a sua modificação, faça o *comitt* e submeta um *pull request*;
* Você também pode abrir uma *issue* com a sua sugestão ou comentário.
