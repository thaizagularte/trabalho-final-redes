import json

# Dicionário para mapear as probes aos seus países
probes_por_pais = {
    "brasil": [32670, 1008770, 6349, 1004982],
    "uruguai": [7147, 1001252, 1004969],
    "argentina": [33508, 31403, 243],
    "gra-bretanha": [17958, 12234, 51756],
    "franca": [32052, 28310, 21536, 61985],
    "russia": [1008493, 18641, 55584],
    "india": [51924, 53099, 64718],
    "china": [1005478, 1005738, 14584, 1005475],
    "japao": [19503, 1005800, 1005363]
}

# Função para identificar o país de uma probe
def identificar_pais(probe_id):
    for pais, probes in probes_por_pais.items():
        if probe_id in probes:
            return pais
    return "desconhecido"

# Função para ler um arquivo JSON
def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados

# Função para extrair informações de um único objeto JSON
def extrair_informacoes(probe):
    # Pegando o id da probe e o timestamp
    prb_id = probe.get("prb_id")
    timestamp = probe.get("timestamp")

    # Identificar o país da probe
    pais = identificar_pais(prb_id)

    # Pegando a quantidade de hops
    quantidade_saltos = len(probe.get("result", []))

    # Pegando a latência do último hop
    if quantidade_saltos > 0:
        ultimo_hop = probe["result"][-1]  # Pega o último hop
        resultados_ultimo_hop = ultimo_hop.get("result", [])

        # Pegando a latência (RTT) do último pacote enviado no último hop
        if len(resultados_ultimo_hop) > 0:
            latencia = resultados_ultimo_hop[-1].get("rtt")
        else:
            latencia = None
    else:
        latencia = None

    return {
        "probe_id": prb_id,
        "pais": pais,
        "timestamp": timestamp,
        "quantidade_saltos": quantidade_saltos,
        "latencia": latencia
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

# Função para gravar os resultados em um novo arquivo JSON
def gravar_resultados_em_json(resultados, caminho_arquivo_saida):
    with open(caminho_arquivo_saida, 'w') as arquivo:
        json.dump(resultados, arquivo, indent=4)

# Exemplo de uso:
lista_arquivos_json = ['prime.json']  # Insira os arquivos aqui
resultado = processar_arquivos_json(lista_arquivos_json)

# Exibir os resultados
for res in resultado:
    print(res)

# Gravar os resultados em um novo arquivo JSON
gravar_resultados_em_json(resultado, 'prime_resultados.json')
