import sys
sys.setrecursionlimit(10000)

def dfs(v, visited, graph):
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor, visited, graph)

while True:
    N, M = map(int, input().split())
    if N == 0 and M == 0:
        break

    # Criação das duas listas de adjacência:
    # 1. Grafo original
    # 2. Grafo transposto (arestas invertidas)
    graph = [[] for _ in range(N + 1)]
    transpose = [[] for _ in range(N + 1)]

    for _ in range(M):
        v, w, p = map(int, input().split())
        graph[v].append(w)
        transpose[w].append(v)
        if p == 2:
            graph[w].append(v)
            transpose[v].append(w)

    # DFS no grafo original
    visited = [False] * (N + 1)
    dfs(1, visited, graph)
    if not all(visited[1:]):
        print(0)
        continue

    # DFS no grafo transposto
    visited = [False] * (N + 1)
    dfs(1, visited, transpose)
    if not all(visited[1:]):
        print(0)
        continue

    # Se passou dos dois testes é fortemente conexo
    print(1)
