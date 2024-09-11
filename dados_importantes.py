import json

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
lista_arquivos_json = ['max.json']  # Insira os arquivos aqui
resultado = processar_arquivos_json(lista_arquivos_json)

# Exibir os resultados
for res in resultado:
    print(res)

# Gravar os resultados em um novo arquivo JSON
gravar_resultados_em_json(resultado, 'max_resultados.json')

