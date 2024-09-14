import pandas as pd
import matplotlib.pyplot as plt

# Carregar os três JSONs
df_disney = pd.read_json('disney_resultados.json')
df_max = pd.read_json('max_resultados.json')
df_prime = pd.read_json('prime_resultados.json')

# Adicionar uma coluna de destino em cada DataFrame para identificar o destino
df_disney['destino'] = 'Disney'
df_max['destino'] = 'Max'
df_prime['destino'] = 'Prime'

# Adicionar uma coluna de país em cada DataFrame (preencha com o país correto para cada DataFrame)
# Exemplo: df_disney['pais'] = 'Brasil'

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

# Adicionar uma coluna de continente ao DataFrame
df_combined = pd.concat([df_disney, df_max, df_prime], ignore_index=True)
df_combined['continente'] = df_combined['pais'].map(continentes)

# Agrupar por 'continente', 'probe_id' e 'destino' para calcular a média da latência
latencia_media = df_combined.groupby(['continente', 'probe_id', 'destino'])['latencia'].mean().reset_index()

# Função para gerar gráfico para um continente específico
def gerar_grafico_continente(continente):
    plt.figure(figsize=(10, 7))
    df_continente = latencia_media[latencia_media['continente'] == continente]
    
    # Obter todas as probes no continente
    probes = df_continente['probe_id'].unique()
    
    for probe in probes:
        df_probe = df_continente[df_continente['probe_id'] == probe]
        plt.plot(df_probe['destino'], df_probe['latencia'], marker='o', label=f'Probe {probe}')
    
    # Configurações do gráfico
    plt.title(f'Latência Média por Probe para {continente}')
    plt.xlabel('Destinos')
    plt.ylabel('Latência Média (ms)')
    plt.legend(title='Probes', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)
    plt.tight_layout()

    # Salvar o gráfico como um arquivo PNG
    plt.savefig(f'latencia_media_{continente.lower().replace(" ", "_")}.png')
    plt.close()

# Gerar gráfico para América do Sul
gerar_grafico_continente('América do Sul')

# Gerar gráfico para Europa
gerar_grafico_continente('Europa')

# Gerar gráfico para Ásia
gerar_grafico_continente('Ásia')
