import pandas as pd
import pyodbc


def criar_dimensao(dataframe: pd.DataFrame, colunas: list, nome_tabela: str):
    """Função para criar as dimensões da tabela. Caso seja a tabela de data, a própria data será a chave estrangeira"""
    dataframe = dataframe[colunas].drop_duplicates().reset_index(drop=True)
    if nome_tabela != "data":
        dataframe["ID" + nome_tabela] = dataframe.index
    return dataframe


# Lendo o csv e realizando as alterações iniciais necessárias
dataset = pd.read_csv("fitness_tracker_dataset.csv")
dataset["date"] = pd.to_datetime(dataset["date"])
dataset["SK"] = dataset.index
dataset = dataset.fillna("Nulo")


# Criando as tabelas dimensões e extraindo as datas
dim_pessoa = criar_dimensao(dataset, ["workout_type", "mood"], "pessoa")
dim_local = criar_dimensao(dataset, list(dataset.iloc[:, 9:11].columns), "local")
dim_data = criar_dimensao(dataset, ["date"], "data")
dim_data["year"] = dim_data["date"].dt.year
dim_data["month"] = dim_data["date"].dt.month
dim_data["day"] = dim_data["date"].dt.day
dim_data["quarter"] = dim_data["date"].dt.quarter


# Criando a tabela fato e conectando com as dimensões
tabela_fato = dataset
tabela_fato = pd.merge(
    tabela_fato,
    dim_pessoa,
    left_on=["workout_type", "mood"],
    right_on=["workout_type", "mood"],
    how="left",
).drop(["workout_type", "mood"], axis=1)

tabela_fato = pd.merge(
    tabela_fato,
    dim_local,
    left_on=["weather_conditions", "location"],
    right_on=["weather_conditions", "location"],
    how="left",
).drop(["weather_conditions", "location"], axis=1)

tabela_fato = pd.merge(tabela_fato, dim_data, on=["date"], how="left").drop(
    ["year", "month", "day", "quarter"], axis=1
)


# Conectando ao banco de dados local
SERVER = r"DESKTOP-6DMIICB\SQLEXPRESS"
DATABASE = "FitnessTracker"

connectionString = (
    f"DRIVER={{ODBC Driver 18 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"Trusted_Connection=yes;"
    f"TrustServerCertificate=yes"
)

try:
    conn = pyodbc.connect(connectionString)
    print("Conexão bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar: {e}")


# Realizando a inserção dos dados
cursor = conn.cursor()


# Inserção de dados na tabela DIM_DATE
data_date = []
for index, row in dim_data.iterrows():
    data_date.append(
        (row["date"], row["year"], row["month"], row["day"], row["quarter"])
    )
cursor.executemany(
    "INSERT INTO DIM_DATE (Date, Year, Month, Day, Quarter) VALUES (?, ?, ?, ?, ?)",
    data_date,
)

# Inserção de dados na tabela DIM_pessoa
data_pessoa = []
for index, row in dim_pessoa.iterrows():
    data_pessoa.append((row["IDpessoa"], row["workout_type"], row["mood"]))
cursor.executemany(
    "INSERT INTO DIM_pessoa (IDpessoa, workout_type, mood) VALUES (?, ?, ?)",
    data_pessoa,
)

# Inserção de dados na tabela DIM_local
data_local = []
for index, row in dim_local.iterrows():
    data_local.append((row["IDlocal"], row["weather_conditions"], row["location"]))
cursor.executemany(
    "INSERT INTO DIM_local (IDLocal, weather_conditions, location) VALUES (?, ?, ?)",
    data_local,
)

# Inserção de dados na tabela tabela_fato
data_tabela_fato = []
for index, row in tabela_fato.iterrows():
    data_tabela_fato.append(
        (
            row["SK"],
            row["user_id"],
            row["date"],
            row["steps"],
            row["calories_burned"],
            row["distance_km"],
            row["active_minutes"],
            row["sleep_hours"],
            row["heart_rate_avg"],
            row["IDpessoa"],
            row["IDlocal"],
        )
    )
cursor.executemany(
    "INSERT INTO FATO   (SK,user_id, DATE, STEPS, calories_burned, distance_km, active_minutes, sleep_hours, heart_rate_avg, IDpessoa, IDlocal) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
    data_tabela_fato,
)

cursor.commit()
conn.close()
print("Inserção realizada")
