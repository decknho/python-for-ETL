# Importando bibliotecas necessárias
import requests 
import json


# Função para extrair dados de um endpoint API
def extract_data(endpoint):
    response = requests.get(endpoint) 
    if response.status_code == 200: # Verifica se a requisição foi bem-sucedida
        return json.loads(response.text)
    else: # Levanta um erro se a requisição não foi bem-sucedida
        response.raise_for_status()


endpoint_users = "https://dummyjson.com/users" # Endpoint para obter dados de usuários
endpoint_products = "https://dummyjson.com/products" # Endpoint para obter dados de produtos

data_users = extract_data(endpoint_users) # Extrai os dados de usuários
data_products = extract_data(endpoint_products) # Extrai os dados de produtos

