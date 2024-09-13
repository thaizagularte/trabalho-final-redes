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

# Combinar todos os DataFrames em um só
df_combined = pd.concat([df_disney, df_max, df_prime], ignore_index=True)

# Agrupar por 'probe_id' e 'destino' para calcular a média da latência
latencia_media = df_combined.groupby(['probe_id', 'destino'])['latencia'].mean().reset_index()

# Agora vamos gerar o gráfico comparativo para as probes
probes = latencia_media['probe_id'].unique()

plt.figure(figsize=(12, 8))

# Para cada probe, vamos plotar a latência em diferentes destinos
for probe in probes:
    df_probe = latencia_media[latencia_media['probe_id'] == probe]
    plt.plot(df_probe['destino'], df_probe['latencia'], marker='o', label=f'Probe {probe}')

# Configurações do gráfico
plt.title('Comparação de Latência por Probe para Diferentes Destinos')
plt.xlabel('Destinos')
plt.ylabel('Latência Média (ms)')
plt.grid(True)

# Configurar a legenda ao lado do gráfico
plt.legend(title='Probes', bbox_to_anchor=(1.05, 1), loc='upper left')

# Ajustar layout para evitar sobreposição
plt.tight_layout()

# Salvar o gráfico como um arquivo PNG
plt.savefig('comparacao_latencia_probes.png')

# Fechar a figura para liberar recursos
plt.close()
