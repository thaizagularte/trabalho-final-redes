import pandas as pd
import json

# Função para converter JSON para CSV
def json_to_csv(json_file, csv_file):
    # Ler o arquivo JSON
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    # Converter o JSON para um DataFrame do pandas
    df = pd.json_normalize(data)
    
    # Salvar o DataFrame como um arquivo CSV
    df.to_csv(csv_file, index=False)
    
    print(f'Arquivo CSV gerado: {csv_file}')

# Exemplo de uso
json_to_csv('prime_resultados.json', 'prime_resultados.csv')
