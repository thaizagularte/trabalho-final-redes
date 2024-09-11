import json
import matplotlib.pyplot as plt

# Função para ler um arquivo JSON
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

# Função para extrair a quantidade de saltos a partir dos resultados
def extrair_quantidade_saltos(resultados):
    timestamps = []
    quantidade_saltos = []
    
    for resultado in resultados:
        timestamp = resultado.get("timestamp")
        saltos = resultado.get("quantidade_saltos")
        
        timestamps.append(timestamp)
        quantidade_saltos.append(saltos)
    
    return timestamps, quantidade_saltos

# Função para criar o gráfico da quantidade de saltos
def criar_grafico_quantidade_saltos(timestamps, quantidade_saltos):
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, quantidade_saltos, marker='o', linestyle='-', color='r')
    plt.xlabel('Timestamp')
    plt.ylabel('Quantidade de Saltos')
    plt.title('Gráfico da Quantidade de Saltos ao Longo do Tempo')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('grafico_quantidade_saltos_prime.png')  # Salva o gráfico como uma imagem
    plt.show()

# Função para extrair informações de um único objeto JSON
def extrair_informacoes(probe):
    # Pegando o id da probe e o timestamp
    prb_id = probe.get("prb_id")
    timestamp = probe.get("timestamp")

    # Pegando a quantidade de hops
    quantidade_saltos = len(probe.get("result", []))

    return {
        "probe_id": prb_id,
        "timestamp": timestamp,
        "quantidade_saltos": quantidade_saltos
    }

# Função principal para processar múltiplos arquivos JSON
def processar_arquivos_json(lista_arquivos):
    resultados = []
    for arquivo in lista_arquivos:
        probes = ler_arquivo_json(arquivo)  # Lê o JSON que é uma lista de objetos

        # Itera sobre cada probe na lista e extrai as informações
        for probe in probes:
            info = extrair_informacoes(probe)
            resultados.append(info)
    
    return resultados

# Exemplo de uso
caminho_arquivo_json = 'prime_resultados.json'  # Caminho do arquivo JSON com os resultados
resultados = processar_arquivos_json([caminho_arquivo_json])

# Extrair quantidade de saltos e timestamps
timestamps, quantidade_saltos = extrair_quantidade_saltos(resultados)

# Criar e exibir o gráfico
criar_grafico_quantidade_saltos(timestamps, quantidade_saltos)
