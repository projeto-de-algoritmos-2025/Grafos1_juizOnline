import sys
import heapq

def tempo_para_str(minutos):
    hora = 17 + minutos // 60
    minuto = minutos % 60
    return f"{hora:02d}:{minuto:02d}"

def main():
    input = sys.stdin.readline

    while True:
        linha = input()
        if not linha.strip():
            continue
        x, n, v = map(int, linha.strip().split())
        if x == 0 and n == 0 and v == 0:
            break

        grafo = {}
        locais = set()

        for _ in range(n):
            o, d, t = input().strip().split()
            t = int(t)
            locais.update([o, d])
            if o not in grafo:
                grafo[o] = []
            grafo[o].append((d, t))

        # Define distâncias iniciais e inicia a fila com 'varzea' no tempo 0
        dist = {local: float('inf') for local in locais}
        dist['varzea'] = 0
        fila = [(0, 'varzea')]

        while fila:
            tempo, atual = heapq.heappop(fila)
            if tempo > dist[atual]:
                continue
            for vizinho, custo in grafo.get(atual, []):
                if dist[vizinho] > tempo + custo:
                    dist[vizinho] = tempo + custo
                    heapq.heappush(fila, (dist[vizinho], vizinho))

        tempo_varzea_alto = dist['alto']

        chegada_ponto = 17 * 60 + x
        if chegada_ponto <= 17 * 60 + 30:
            partida = 17 * 60 + 30
        else:
            partida = 17 * 60 + 50

        chegada_fim = partida + tempo_varzea_alto
        print(tempo_para_str(chegada_fim - 17 * 60))
        print("Nao ira se atrasar" if chegada_fim <= 18 * 60 else "Ira se atrasar")

if __name__ == "__main__":
    main()
