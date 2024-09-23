

# Código que recebe um resultado da medição e gera o gráficos da latencia 
# por timestamp para cada destino sendo separado por  países

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

# Mapeamento de país para continente
continentes = {
    'franca': 'Europa',
    'russia': 'Europa',
    'china': 'Ásia',
    'japao': 'Ásia',
    'brasil': 'América do Sul',
    'argentina': 'América do Sul',
    'uruguai': 'América do Sul',
    'gra-bretanha': 'Europa',
    'india': 'Ásia'
}

# Adicionar uma coluna de continente ao DataFrame
df_combined = pd.concat([df_disney, df_max, df_prime], ignore_index=True)
df_combined['continente'] = df_combined['pais'].map(continentes)

# Gerar gráficos comparativos para cada continente
continentes_unicos = df_combined['continente'].unique()

for continente in continentes_unicos:
    # Filtrar dados do continente atual
    df_continente = df_combined[df_combined['continente'] == continente]
    
    # Verificar se há dados para esse continente
    if df_continente.empty:
        continue

    plt.figure(figsize=(14, 8))

    # Obter todos os países do continente atual
    paises = df_continente['pais'].unique()

    # Plotar a latência para cada país em cada destino
    for pais in paises:
        for destino in df_continente['destino'].unique():
            df_pais_destino = df_continente[(df_continente['pais'] == pais) & (df_continente['destino'] == destino)]
            plt.plot(df_pais_destino['timestamp'], df_pais_destino['latencia'], marker='o', label=f'{pais} -> {destino}')

    # Configurações do gráfico
    plt.title(f'Latência por país e destino no continente {continente}')
    plt.xlabel('Timestamp')
    plt.ylabel('Latência (ms)')
    plt.legend(title='País -> Destino', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    # Ajustar layout para evitar sobreposição
    plt.tight_layout()

    # Salvar o gráfico como um arquivo PNG
    plt.savefig(f'latencia_{continente}.png')

    # Fechar a figura para liberar recursos
    plt.close()
