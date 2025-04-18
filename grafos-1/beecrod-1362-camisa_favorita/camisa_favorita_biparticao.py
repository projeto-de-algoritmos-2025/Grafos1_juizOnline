# -*- coding: utf-8 -*-

# Aqui o sys aumenta o tamanho da recursão que será utilizada na função DFS 
import sys
sys.setrecursionlimit(10000)

# Mapeia os tamanhos de camiseta para índices para facilitar a manipulacao de dado para o grafo
tamanho_para_indice = {
    'XS': 0,
    'S': 1,
    'M': 2,
    'L': 3,
    'XL': 4,
    'XXL': 5
}

def pode_distribuir(n, m, preferencias):
    # Quantidade de camisetas por tamanho
    # cria uma lista de listas
    qtd_por_tamanho = n // 6
    total_camisas = [[] for _ in range(6 * qtd_por_tamanho)]
    
    # Cada camiseta tem um id único (0 a n-1), agrupadas por tamanho
    camiseta_id_por_tamanho = [[] for _ in range(6)]
    idx = 0
    for t in range(6):
        for _ in range(qtd_por_tamanho):
            camiseta_id_por_tamanho[t].append(idx)
            idx += 1

    # Cria grafo de preferências: voluntário -> camisetas compatíveis
    # sendo t1 e t2 as camisas a serem adicionadas ( via append) a nossa lista de listas
    grafo = [[] for _ in range(m)]
    for i in range(m):
        t1, t2 = preferencias[i]
        for cid in camiseta_id_por_tamanho[tamanho_para_indice[t1]]:
            grafo[i].append(cid)
        for cid in camiseta_id_por_tamanho[tamanho_para_indice[t2]]:
            grafo[i].append(cid)

    match = [-1] * (n)  # match[c] = voluntário atribuído à camiseta c

    # Função de busca em profundidade (dfs) ele serve para verificar se ja foi visitado o vertice do grafo, e caso tenha sido visitado ( nessa chamada) ele continua, caso ele
    # não tenha sido visitado porém a camisa foi selecionada por uma chamada anterior, ele vai de forma recursiva entre chamadas para tentar realocal a camisa da pessoa anterior, caso seja
    # possivel realocar ele volta e tenta de novo o dfs, se não ele retorna falso.
    def dfs(u, visitado):
        for v in grafo[u]:
            if not visitado[v]:
                visitado[v] = True
                if match[v] == -1 or dfs(match[v], visitado):
                    match[v] = u
                    return True
        return False
    # total match é quantas camisas ja deram match entre quem quer e quem ja possui a camisa desse tamanho
    # visitado é uma lista de falsos, que toda vez que é visitado o dfs ele muda seu status para true, quando todos os dfs terminam de rodar e todos são visitados
    # se o grafo for bipartido ele deve retornar uma lista completa de trues ( ou seja total_match == m)
    total_match = 0
    for u in range(m):
        visitado = [False] * n
        if dfs(u, visitado):
            total_match += 1

    return total_match == m

# Lê entrada e tenta padronizar para o caso de ter espaços desnecessarios na entrada que possam criar poluicao no codigo ( e gere erros )
# t1 e t2 são os tamanhos preferiveis pelas pessoas n é a quantidade de camisetas disponiveis e m o numero de pessoas que querem esses valores 
T = int(sys.stdin.readline())
for _ in range(T):
    linha = ''
    while linha.strip() == '':
        linha = sys.stdin.readline()
    n, m = map(int, linha.strip().split())
    preferencias = []
    for _ in range(m):
        while True:
            linha = sys.stdin.readline().strip()
            if linha:
                break
        t1, t2 = linha.split()
        preferencias.append((t1, t2))

    print("YES" if pode_distribuir(n, m, preferencias) else "NO")