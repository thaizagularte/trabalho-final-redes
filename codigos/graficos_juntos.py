import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para ler múltiplos arquivos JSON e combinar em um DataFrame
def ler_e_combinar_jsons(lista_arquivos_json):
    dfs = []
    for arquivo in lista_arquivos_json:
        with open(arquivo, 'r') as f:
            dados = json.load(f)
        df = pd.DataFrame(dados)
        dfs.append(df)
    return pd.concat(dfs, ignore_index=True)

# Função para ajustar os timestamps para horas
def ajustar_timestamp_para_horas(df):
    df['horas'] = df['timestamp'] / 3600  # Convertendo segundos para horas
    return df

# Função para gerar gráficos comparando latência entre destinos por país
def grafico_comparar_destinos_latencia(df, salvar=False):
    plt.figure(figsize=(12, 7))
    sns.lineplot(x='horas', y='latencia', hue='destino', data=df, marker='o')
    plt.title('Comparação de Latência entre Destinos ao Longo do Tempo')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Latência (ms)')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/comparacao_latencia_destinos.png', dpi=300, bbox_inches='tight')
    plt.show()

# Função para gerar gráficos comparando saltos entre destinos por país
def grafico_comparar_destinos_saltos(df, salvar=False):
    plt.figure(figsize=(12, 7))
    sns.lineplot(x='horas', y='quantidade_saltos', hue='destino', data=df, marker='o')
    plt.title('Comparação de Saltos entre Destinos ao Longo do Tempo')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Quantidade de Saltos')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/comparacao_saltos_destinos.png', dpi=300, bbox_inches='tight')
    plt.show()

# Função para gerar gráficos de correlação entre latência e saltos comparando destinos
def grafico_comparar_destinos_correlacao(df, salvar=False):
    plt.figure(figsize=(12, 7))
    sns.scatterplot(x='quantidade_saltos', y='latencia', hue='destino', data=df)
    plt.title('Correlação entre Latência e Saltos Comparando Destinos')
    plt.xlabel('Quantidade de Saltos')
    plt.ylabel('Latência (ms)')
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/comparacao_correlacao_destinos.png', dpi=300, bbox_inches='tight')
    plt.show()

# Exemplo de uso:
lista_arquivos_json = ['disney_resultados.json', 'max_resultados.json', 'prime_resultados.json']  # Arquivos para os 3 destinos
dados = ler_e_combinar_jsons(lista_arquivos_json)

# Ajustar timestamps para horas
dados = ajustar_timestamp_para_horas(dados)

# Gerando gráficos de comparação entre destinos e salvando como PNG
grafico_comparar_destinos_latencia(dados, salvar=True)
grafico_comparar_destinos_saltos(dados, salvar=True)
grafico_comparar_destinos_correlacao(dados, salvar=True)
