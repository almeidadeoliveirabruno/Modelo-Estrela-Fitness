# Introdução


## Objetivo
O objetivo desse projeto é fazer uma revisão de modelo estrela, PowerBi e Pandas. O dataset "Fitness_tracker_dataset.scv" foi baixado do site [Kaggle](https://www.kaggle.com/datasets/arnavsmayan/fitness-tracker-dataset) para a realização deste projeto. Ao chegar na parte de fazer a análise propriamente dita, percebi que os dados parecem ter sido gerados e eles não possuem muita lógica, portanto esse projeto foi finalizado após a integração dos dados do sql server com o PowerBi.


Este dataset contém dados sintéticos coletados de dispositivos de rastreamento de atividades físicas, abrangendo informações sobre as atividades diárias dos usuários, rotinas de exercícios, frequência cardíaca, padrões de sono e consumo calórico. Ele foi projetado para analisar tendências de saúde e condicionamento físico, otimizar planos de treino e promover escolhas de estilo de vida mais saudáveis.

Colunas:

- user_id: Identificador único para cada usuário.
- date: Data da coleta dos dados.
- steps: Número de passos dados.
- calories_burned: Total de calorias queimadas.
- distance_km: Distância percorrida em quilômetros.
- active_minutes: Minutos gastos em atividades físicas.
- sleep_hours: Horas de sono registradas.
- heart_rate_avg: Frequência cardíaca média.
- workout_type: Tipo de exercício realizado (ex.: Corrida, Caminhada, Ciclismo).
- weather_conditions: Condições climáticas durante a atividade (ex.: Limpo, Chuva, Neve, Nevoeiro).
- location: Local onde a atividade foi realizada (ex.: Casa, Academia, Parque).
- mood: Humor do usuário (ex.: Feliz, Neutro, Cansado, Estressado).


## Tecnologias Utilizadas
| Tecnologia     | Ícone              |               Finalidade    |     
|---------------|------------------ |-------------- |
| Python  | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"   width="40"/>  | Linguagem de programação utilizada |
| Pyodb  | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="40"/>  | Conexão com o banco de dados  |
| Black  | <img src="Imagens/image-7.png" height="35"/>  | Formatação automática do código de acordo com a PEP 8 |
| Pandas  | <img src="Imagens/image-4.png" alt="Pandas" width="50"/>  | Manipulação dos dados  |
| Sql Server  | <img src="Imagens/image-5.png" alt="Sql Server" width="50"/> | Banco de dados utilizado  |
| Power BI  | <img src="Imagens/image-8.svg" alt="Power BI" width="50"/> | Para testar o desempenho do CSV e modelo Estrela  |


## Projeto

### Planejamento de modelagem e criação do banco de dados.
1. **Visão Geral dos dados**                                                
    Foi utilizado o Pandas para realizar uma análise exploratória dos dados, identificando possíveis inconsistências e auxiliando na definição precisa dos tipos de dados ao transferi-los para o banco de dados. A análise completa pode ser conferida neste [notebook](dados_Visão_geral.ipynb).

2. **Criação Banco de Dados**                                                
    Com base nos tipos de dados identificados durante a análise exploratória, a base de dados foi criada localmente, garantindo uma estrutura alinhada às necessidades do projeto. O script utilizado para criar o banco pode ser consultado no [arquivo SQL](Base%20de%20dados%20SQL.sql). Abaixo, pode ser visto o diagrama do modelo estrela:


<img src="Imagens/Modelo Estrela.png" alt="">


### Modelagem

1. **Criação das entidades**  
   A modelagem foi realizada utilizando a biblioteca Pandas do Python. O arquivo CSV foi carregado como um DataFrame, e entidades representando as tabelas do modelo estrela foram criadas. IDs únicos foram gerados para cada entidade, garantindo a normalização dos dados.

2. **Conexões entre as tabelas**  
   O método `merge` do Pandas foi utilizado para estabelecer as relações entre os DataFrames, permitindo substituir as colunas da tabela fato pelas respectivas chaves estrangeiras. Em seguida, a biblioteca pyodbc foi empregada para estabelecer a conexão com o banco de dados local e inserir os valores diretamente a partir dos DataFrames.

3. **Conformidade com padrões de código**  
   As bibliotecas **Black** e **isort** foram utilizadas para garantir que o código estivesse alinhado às melhores práticas recomendadas pela PEP 8, promovendo legibilidade e organização.

4. **Importação para o Powerbi**  
   O modo de conectividade escolhido foi o importar. O directQuery demonstrou um desempenho inferior nesta situação.


