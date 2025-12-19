from community import community_louvain
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import networkx as nx


def criar_grafo_de_arquivo(caminho_do_arquivo):
    grafo = nx.Graph()
    with open(caminho_do_arquivo, 'r') as arquivo:
        for linha in arquivo:
            
            linha = linha.strip().split()
            # Split the cleaned line into values
            if(len(linha) == 2 ):
                u, v = map(int, linha[:2])
                #print("linha:", linha)
                #u, v = map(int, linha.strip().split())
                grafo.add_edge(u, v)
            else:
                print("Erro: Linha com menos de dois valores:", linha)
    return grafo

def aplicar_louvain_e_visualizar(grafo):
    # Encontrar a partição com o algoritmo de Louvain
    partition = community_louvain.best_partition(grafo)

    # Visualização do grafo
    pos = nx.spring_layout(grafo)
    cmap = plt.get_cmap('viridis')
    colors = [cmap(float(partition[node])) for node in grafo.nodes()]

    nx.draw_networkx_nodes(grafo, pos, node_size=100, node_color=colors)
    nx.draw_networkx_edges(grafo, pos, alpha=0.5)
    plt.show()

    return partition

# Caminho do arquivo que contém as arestas
#caminho_do_arquivo = 'IrisDataVertices.txt'
#caminho_do_arquivo = 'ArqVerticesGrafo.txt'
caminho_do_arquivo = 'Grafo_HAWKS.txt'

# Criar o grafo a partir do arquivo
grafo = criar_grafo_de_arquivo(caminho_do_arquivo)

# Aplicar o algoritmo de Louvain e visualizar os clusters
clusters = aplicar_louvain_e_visualizar(grafo)
print("Clusters encontrados:", clusters)


#3##################3

#######################3



#######################
