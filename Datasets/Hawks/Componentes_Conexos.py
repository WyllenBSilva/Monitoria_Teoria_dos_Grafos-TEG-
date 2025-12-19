import gc

# Seu código para processar dados...

# Coleta de lixo para liberar memória


def criar_grafo_de_arquivo(caminho_do_arquivo):
    grafo = {}
    with open(caminho_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            valores = linha.strip().split()

            if(len(valores) >= 2):

                u, v = map(int, valores[:2])
                if u not in grafo:
                    grafo[u] = []
                if v not in grafo:
                    grafo[v] = []
                grafo[u].append(v)
                grafo[v].append(u)  # Assumindo um grafo não-direcionado
            else:
                print("Erro: Linha com menos de dois valores:", linha)
            #gc.collect()
    return grafo

def dfs(grafo, vertice, visitado):
    visitado.add(vertice)
    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitado:
            dfs(grafo, vizinho, visitado)

def encontrar_componentes_conexos(grafo):
    visitado = set()
    componentes = 0

    for vertice in grafo:
        if vertice not in visitado:
            dfs(grafo, vertice, visitado)
            componentes += 1
    return componentes

# Caminho do arquivo que contém as arestas
caminho_do_arquivo = 'ArqVerticesGrafo.txt'
#caminho_do_arquivo = 'IrisDataVertices.txt'

# Criar o grafo a partir do arquivo
grafo = criar_grafo_de_arquivo(caminho_do_arquivo)

# Encontrar os componentes conexos
componentes = encontrar_componentes_conexos(grafo)
print("Número de componentes conexos:", componentes)
