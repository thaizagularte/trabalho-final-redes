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
# Se os dados não tiverem a coluna 'pais', adicione conforme necessário
# Exemplo: df_disney['pais'] = 'Brasil' 
# Preencha com o país correto para cada DataFrame

# Combinar todos os DataFrames em um só
df_combined = pd.concat([df_disney, df_max, df_prime], ignore_index=True)

# Agrupar por 'pais', 'probe_id' e 'destino' para calcular a média da latência
latencia_media = df_combined.groupby(['pais', 'probe_id', 'destino'])['latencia'].mean().reset_index()

# Gerar o gráfico comparativo para todas as probes agrupadas por país
plt.figure(figsize=(14, 10))

# Obter todos os países
paises = latencia_media['pais'].unique()

for pais in paises:
    df_pais = latencia_media[latencia_media['pais'] == pais]
    
    # Para cada probe no país, plotar a latência em diferentes destinos
    probes = df_pais['probe_id'].unique()
    for probe in probes:
        df_probe = df_pais[df_pais['probe_id'] == probe]
        plt.plot(df_probe['destino'], df_probe['latencia'], marker='o', label=f'{pais} - Probe {probe}')

# Configurações do gráfico
plt.title('Comparação de Latência por Probe para Diferentes Destinos e Países')
plt.xlabel('Destinos')
plt.ylabel('Latência Média (ms)')
plt.legend(title='Legenda', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Salvar o gráfico como um arquivo PNG
plt.savefig('comparacao_latencia_probes_paises.png')

# Fechar a figura para liberar recursos
plt.close()
