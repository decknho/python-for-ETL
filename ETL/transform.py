# Importando bibliotecas necessárias para transformação de dados
import pandas as pd # Biblioteca para manipulação de dados em DataFrames
from ETL.extract import data_users, data_products # Importa os dados extraídos dos endpoints API


df_users = pd.DataFrame(data_users['users']) # Converte os dados de usuários em DataFrame
df_products = pd.DataFrame(data_products['products']) # Converte os dados de produtos em DataFrame


# Criando DataFrames separando informações de contas do "df_users" para ser usado como tabelas para popular um banco de dados posteriormente
df_contas = df_users[['id','email', 'username', 'password', 'role']].copy()
df_dadosPessoais = df_users[['id', 'firstName', 'lastName', 'phone', 'birthDate']].rename(columns={'id': 'user_id'}).copy()

# Criando DataFrame separando informações de produtos do "df_products" para ser usado como tabelas para popular um banco de dados posteriormente
