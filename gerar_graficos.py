import json
import matplotlib.pyplot as plt

# Função para ler um arquivo JSON
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

# Função para extrair informações de latência a partir dos resultados
def extrair_latencias(resultados):
    timestamps = []
    latencias = []
    
    for resultado in resultados:
        timestamp = resultado.get("timestamp")
        latencia = resultado.get("latencia")
        
        if latencia is not None:
            timestamps.append(timestamp)
            latencias.append(latencia)
    
    return timestamps, latencias

# Função para criar o gráfico de latência
def criar_grafico_latencia(timestamps, latencias):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, latencias, marker='o', linestyle='-', color='b')
    plt.xlabel('Timestamp')
    plt.ylabel('Latência (ms)')
    plt.title('Gráfico de Latência ao Longo do Tempo')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_latencia_prime.png')  # Salva o gráfico como uma imagem
    plt.show()

# Exemplo de uso
caminho_arquivo_json = 'prime_resultados.json'  # Caminho do arquivo JSON com os resultados
resultados = ler_arquivo_json(caminho_arquivo_json)

# Extrair latências e timestamps
timestamps, latencias = extrair_latencias(resultados)

# Criar e exibir o gráfico
criar_grafico_latencia(timestamps, latencias)
