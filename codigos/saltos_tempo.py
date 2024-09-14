import json
import matplotlib.pyplot as plt

#Funções que retornam a latencia por tempo de cada pais e continentes

def probes_paises():
    with open('max_resultados.json') as f1, open('disney_resultados.json') as f2, open('prime_resultados.json') as f3:
        dados1 = json.load(f1)
        dados2 = json.load(f2)
        dados3 = json.load(f3)

    dados = dados1 + dados2 + dados3

    probes_por_pais_destino = {}
    for item in dados:
        pais = item['pais']
        destino = item['destino']
        
        chave = (pais, destino)
        if chave not in probes_por_pais_destino:
            probes_por_pais_destino[chave] = []
        
        probes_por_pais_destino[chave].append(item)

    plt.figure(figsize=(12,8))

    for (pais, destino), probes in probes_por_pais_destino.items():
        probes_ordenadas = sorted(probes, key=lambda x: x['timestamp'])
        timestamps = [probe['timestamp'] for probe in probes_ordenadas]
        saltos = [probe['quantidade_saltos'] for probe in probes_ordenadas]
        
        label = f'{pais} - {destino}'
        plt.plot(timestamps, saltos, label=label)

    plt.title('Quant. de saltos ao longo do tempo por país e destino')
    plt.xlabel('Timestamp')
    plt.ylabel('Quant. de saltos')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    plt.tight_layout()

    plt.savefig('comparacao_saltos_probes_pais.png')

    plt.show()

def probes_continentes():
    mapa_continentes = {
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
    
    with open('max_resultados.json') as f1, open('disney_resultados.json') as f2, open('prime_resultados.json') as f3:
        dados1 = json.load(f1)
        dados2 = json.load(f2)
        dados3 = json.load(f3)

    dados = dados1 + dados2 + dados3

    probes_por_continente_destino = {}
    for item in dados:
        pais = item['pais']
        destino = item['destino']
        
        continente = mapa_continentes.get(pais, 'Desconhecido')
        
        if continente == 'Desconhecido':
            print(f"Continente desconhecido para o país: {pais}")
        
        chave = (continente, destino)
        if chave not in probes_por_continente_destino:
            probes_por_continente_destino[chave] = []
        probes_por_continente_destino[chave].append(item)

    plt.figure(figsize=(12,8))

    for (continente, destino), probes in probes_por_continente_destino.items():
        probes_ordenadas = sorted(probes, key=lambda x: x['timestamp'])
        timestamps = [probe['timestamp'] for probe in probes_ordenadas]
        saltos = [probe['quantidade_saltos'] for probe in probes_ordenadas]
        
        label = f'{continente} - {destino}'
        
        plt.plot(timestamps, saltos, label=label)

    plt.title('Quant. de saltos ao longo do tempo por continente e destino')
    plt.xlabel('Timestamp')
    plt.ylabel('Quant. de saltos (ms)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('comparacao_saltos_probes_continentes.png')
    plt.show()

probes_continentes()
probes_paises()
