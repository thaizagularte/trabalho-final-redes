import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#GERA GRAFICOS DE CADA MEDIÇÃO


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

# Função para gerar gráficos de latência ao longo do tempo por país e destino
def grafico_latencia(df, salvar=False):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='horas', y='latencia', hue='pais', data=df, marker='o')
    plt.title('Variação da Latência ao Longo do Tempo por País')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Latência (ms)')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_latencia_max.png', dpi=300, bbox_inches='tight')
    plt.show()

# Função para gerar gráficos de quantidade de saltos ao longo do tempo por país e destino
def grafico_saltos(df, salvar=False):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='horas', y='quantidade_saltos', hue='pais', data=df, marker='o')
    plt.title('Variação da Quantidade de Saltos ao Longo do Tempo por País')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Quantidade de Saltos')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_saltos_max.png', dpi=300, bbox_inches='tight')
    plt.show()

# Função para gerar gráficos de correlação entre latência e quantidade de saltos para países
def grafico_correlacao_paises(df, salvar=False):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='quantidade_saltos', y='latencia', hue='pais', data=df, marker='o')  # Trocar para quantidade de saltos no eixo X
    plt.title('Correlação entre Latência e Quantidade de Saltos por País')
    plt.xlabel('Quantidade de Saltos')
    plt.ylabel('Latência (ms)')
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_correlacao_paises_max.png', dpi=300, bbox_inches='tight')  # Nome diferente para salvar
    plt.show()

# Função para gerar gráficos de correlação entre latência e quantidade de saltos para continentes
def grafico_correlacao_continentes(df, salvar=False):
    df['continente'] = df['pais'].map(continentes)

    plt.figure(figsize=(10, 6))
    sns.lineplot(x='quantidade_saltos', y='latencia', hue='continente', data=df, marker='o')  # Trocar para quantidade de saltos no eixo X
    plt.title('Correlação entre Latência e Quantidade de Saltos por Continente')  # Título ajustado
    plt.xlabel('Quantidade de Saltos')
    plt.ylabel('Latência (ms)')
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_correlacao_continentes_max.png', dpi=300, bbox_inches='tight')  # Nome diferente para salvar
    plt.show()

# Função para gerar gráficos por continente (necessita de um mapeamento de país -> continente)
def grafico_por_continente(df, continentes, salvar=False):
    df['continente'] = df['pais'].map(continentes)

    # Gráfico de latência por continente
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='horas', y='latencia', hue='continente', data=df, marker='o')
    plt.title('Variação da Latência ao Longo do Tempo por Continente')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Latência (ms)')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_latencia_continente_max.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Gráfico de saltos por continente
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='horas', y='quantidade_saltos', hue='continente', data=df, marker='o')
    plt.title('Variação da Quantidade de Saltos ao Longo do Tempo por Continente')
    plt.xlabel('Tempo (Horas)')
    plt.ylabel('Quantidade de Saltos')
    plt.xticks(rotation=45)
    plt.grid(True)
    if salvar:
        plt.savefig('../graficos/max/grafico_saltos_continente_max.png', dpi=300, bbox_inches='tight')
    plt.show()

# Exemplo de uso:
lista_arquivos_json = ['.json']  # Substituir pelos nomes dos seus arquivos
dados = ler_e_combinar_jsons(lista_arquivos_json)

# Ajustar timestamps para horas
dados = ajustar_timestamp_para_horas(dados)

# Mapeamento de país para continente
continentes = {
    'franca': 'Europa',
    'russia': 'Europa',
    'china': 'Ásia',
    'japao': 'Ásia',
    'brasil': 'América do Sul',
    'argentina': 'América do Sul',
    'uruguai': 'América do Sul',
    'gra-bretania': 'Europa',
    'india': 'Ásia'
}

# Gerando gráficos e salvando como PNG
grafico_latencia(dados, salvar=True)
grafico_saltos(dados, salvar=True)
grafico_correlacao_paises(dados, salvar=True)
grafico_correlacao_continentes(dados, salvar=True)
grafico_por_continente(dados, continentes, salvar=True)
