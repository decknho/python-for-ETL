# Importando bibliotecas necessárias para transformação de dados
import pandas as pd # Biblioteca para manipulação de dados em DataFrames
from extract import data_users, data_products # Importa os dados extraídos dos endpoints API


df_users = pd.DataFrame(data_users['users']) # Converte os dados de usuários em DataFrame
df_products = pd.DataFrame(data_products['products']) # Converte os dados de produtos em DataFrame

df_users.to_csv("data/users.csv", index=False) # Salva o DataFrame de usuários em um arquivo CSV
df_products.to_json("data/products.json", orient="records", lines=True) # Salva o DataFrame de produtos em um arquivo JSON