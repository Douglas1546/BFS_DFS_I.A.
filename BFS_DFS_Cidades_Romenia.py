from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import os

os.system('cls')

Rotas = dict()

Rotas['Arad'] = {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}
Rotas['Bucharest'] = {'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85, 'Fagaras': 211}
Rotas['Craiova'] = {'Drobeta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146}
Rotas['Drobeta'] =  {'Craiova': 120, 'Mehadia': 75}
Rotas['Eforie'] = {'Hârlău': 87}
Rotas['Fagaras'] = {'Bucharest': 211, 'Sibiu': 99}
Rotas['Giurgiu'] = {'Bucharest': 90}
Rotas['Hârlău'] = {'Eforie': 87, 'Iasi': 92, 'Urziceni': 98}
Rotas['Iasi'] = {'Hârlău': 92, 'Neamt': 87, 'Vaslui': 92}
Rotas['Lugoj'] = {'Timisoara': 111, 'Mehadia': 70}
Rotas['Mehadia']  = {'Lugoj': 70, 'Drobeta': 75}
Rotas['Neamt']  =  {'Iasi': 87}
Rotas['Oradea']  = {'Zerind': 71, 'Sibiu': 151} 
Rotas['Pitesti'] = {'Bucharest': 101, 'Rimnicu Vilcea': 97, 'Craiova': 138}
Rotas['Rimnicu Vilcea'] = {'Pitesti': 97, 'Sibiu': 80, 'Craiova': 146}
Rotas['Sibiu'] =  {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80}
Rotas['Timisoara']  = {'Arad': 118, 'Lugoj': 111}
Rotas['Urziceni'] = {'Bucharest': 85, 'Hârlău': 98, 'Vaslui': 142}
Rotas['Vaslui'] = {'Iasi': 92, 'Urziceni': 142}
Rotas['Zerind'] = {'Arad': 75, 'Oradea': 71}

#===================================================================================================================================================#

#função busca em largura e exibe os caminhos passados
print("===========================================================================================================================================")
print("Busca em largura com custo: \n")

def busca_largura_com_custo(grafo, inicio, fim):
    fila = deque([(inicio, 0, [inicio])])  # Inicializa a fila com o vértice de início, o custo acumulado 0 e o caminho percorrido
    visitados = set()
    
    # Cria o grafo utilizando o dicionário 'grafo'
    G = nx.Graph(grafo)
    
    while fila:
        vertice, custo_acumulado, caminho = fila.popleft() # Remove o primeiro elemento da fila
        if vertice == fim:
            print("Caminho encontrado:", caminho)
            print("Custo acumulado:", custo_acumulado)
            
            # Desenha o grafo
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
            
            # Marca o caminho percorrido no grafo
            path_edges = list(zip(caminho, caminho[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0)
            
            # Exibe o desenho do grafo
            plt.show()
            
            return  # Encerra a busca após encontrar o primeiro caminho
        if vertice not in visitados: # Verifica se o vértice atual já foi visitado
            for vizinho in grafo.get(vertice, []): # Obtém os vizinhos do vértice atual
                custo = grafo[vertice][vizinho]  # Obtém o custo da aresta entre o vértice atual e o vizinho
                novo_custo_acumulado = custo_acumulado + custo # Calcula o custo acumulado até o momento
                novo_caminho = caminho + [vizinho] # Calcula o caminho percorrido até o momento
                fila.append((vizinho, novo_custo_acumulado, novo_caminho)) # Adiciona o vizinho na fila
            visitados.add(vertice)
    print("Caminho não encontrado.")
    return None

busca_largura_com_custo(Rotas, 'Arad', 'Bucharest')

#===================================================================================================================================================#

#função para busca em profundidade e exibe os caminhos passados
print("\n===========================================================================================================================================\n")
print("Busca em profundidade com custo: \n")

def busca_profundidade_com_custo(grafo, inicio, fim):
    pilha = [[inicio, 0, [inicio]]]  # Inicializa a pilha com o vértice de início, o custo acumulado 0 e o caminho percorrido
    visitados = set()
    
    # Cria o grafo utilizando o dicionário 'grafo'
    G = nx.Graph(grafo)
    
    while pilha:
        vertice, custo_acumulado, caminho = pilha.pop() # Remove o último elemento da pilha
        visitados.add(vertice) # Marca o vértice atual como visitado
        if vertice == fim:
            print("Caminho encontrado:", caminho)
            print("Custo acumulado:", custo_acumulado)
            
            # Desenha o grafo
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
            
            # Marca o caminho percorrido no grafo
            path_edges = list(zip(caminho, caminho[1:]))
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2.0)
            
            # Exibe o desenho do grafo
            plt.show()
            
            return  # Encerra a busca após encontrar o primeiro caminho
        for vizinho in grafo.get(vertice, []): # Obtém os vizinhos do vértice atual
            if vizinho not in visitados: # Verifica se o vértice atual já foi visitado
                custo = grafo[vertice][vizinho]  # Obtém o custo da aresta entre o vértice atual e o vizinho
                novo_custo_acumulado = custo_acumulado + custo # Calcula o custo acumulado até o momento
                novo_caminho = caminho + [vizinho] # Calcula o caminho percorrido até o momento
                pilha.append([vizinho, novo_custo_acumulado, novo_caminho]) # Adiciona o vizinho na pilha
    print("Caminho não encontrado.")
    return None

busca_profundidade_com_custo(Rotas, 'Arad', 'Bucharest')

print("\n===========================================================================================================================================\n")


