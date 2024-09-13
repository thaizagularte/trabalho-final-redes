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

# Filtrar apenas as probes da América do Sul
df_south_america = df_combined[df_combined['continente'] == 'América do Sul']

# Agrupar por 'destino', 'timestamp' e calcular a média da latência
latencia_media_south_america = df_south_america.groupby(['destino', 'timestamp'])['latencia'].mean().reset_index()

# Gerar o gráfico comparativo para a latência média da América do Sul
plt.figure(figsize=(14, 8))

# Obter todos os destinos
destinos = latencia_media_south_america['destino'].unique()

for destino in destinos:
    df_destino = latencia_media_south_america[latencia_media_south_america['destino'] == destino]
    plt.plot(df_destino['timestamp'], df_destino['latencia'], marker='o', label=f'Destino: {destino}')

# Configurações do gráfico
plt.title('Comparação de Latência Média da América do Sul ao Longo do Tempo para Diferentes Destinos')
plt.xlabel('Timestamp')
plt.ylabel('Latência Média (ms)')
plt.legend(title='Destinos', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Salvar o gráfico como um arquivo PNG
plt.savefig('comparacao_latencia_south_america.png')

# Fechar a figura para liberar recursos
plt.close()

