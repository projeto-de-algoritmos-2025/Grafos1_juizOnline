# deque e uma biblioteca que serve para criar filas  e defaultdict para criar um grafo de lista de adjacencia
from collections import deque, defaultdict

#função que define o caminho inicial como Entrada e valida o set para aqueles que ja foram visitados
def bfs_path(grafo, origem, destino):
    fila = deque([[origem]])
    visitados = set([origem])
    
    #Tira o caminho atual da fila
    while fila:
        caminho = fila.popleft()
        atual = caminho[-1]
        # se o  caminho for igual ao destino 
        if atual == destino:
            return caminho  # retorna lista de pontos visitados
        #expande em largura, ou seja visita  cada vizinho do nó atual e marca ele, é o método crucial para criação do cmainho otimizado em uma bfs
        for vizinho in grafo[atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                nova = list(caminho)
                nova.append(vizinho)
                fila.append(nova)

    return []
# main que vai chamar o caminho ( labirinto do rato )
def main():
    P, L = map(int, input().split())
    grafo = defaultdict(list)

    for _ in range(L):
        u, v = input().split()
        grafo[u].append(v)
        grafo[v].append(u)

    caminho1 = bfs_path(grafo, "Entrada", "*")
    caminho2 = bfs_path(grafo, "*", "Saida")

    if not caminho1 or not caminho2:
        print(0)
    else:
        # soma dos dois caminhos, sem remover o "*"
        total_pontos = len(caminho1) + len(caminho2)
        print(total_pontos)

if __name__ == "__main__":
    main()
