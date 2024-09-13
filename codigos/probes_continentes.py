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

# Adicionar uma coluna de país em cada DataFrame (assumindo que você tem essa informação)
# Exemplo: df_disney['pais'] = 'Brasil'
# Preencha com o país correto para cada DataFrame

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

# Gerar o gráfico comparativo para todas as probes agrupadas por continente
plt.figure(figsize=(14, 10))

# Obter todos os continentes
continentes_unicos = latencia_media['continente'].unique()

for continente in continentes_unicos:
    df_continente = latencia_media[latencia_media['continente'] == continente]
    
    # Para cada probe no continente, plotar a latência em diferentes destinos
    probes = df_continente['probe_id'].unique()
    for probe in probes:
        df_probe = df_continente[df_continente['probe_id'] == probe]
        plt.plot(df_probe['destino'], df_probe['latencia'], marker='o', label=f'{continente} - Probe {probe}')

# Configurações do gráfico
plt.title('Comparação de Latência por Probe para Diferentes Destinos e Continentes')
plt.xlabel('Destinos')
plt.ylabel('Latência Média (ms)')
plt.legend(title='Legenda', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Salvar o gráfico como um arquivo PNG
plt.savefig('comparacao_latencia_probes_continentes.png')

# Fechar a figura para liberar recursos
plt.close()
