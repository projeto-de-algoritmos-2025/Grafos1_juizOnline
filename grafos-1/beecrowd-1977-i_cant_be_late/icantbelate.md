# Relatório – Problema "I Can’t Be Late" (Beecrowd 1977)

![questao_icantbelate](../../assets/lista1/icant_1977/icantbelate.png)

![erro_icantbelate](../../assets/lista1/icant_1977/icantbelate_erro.png)

## Contextualização

O problema pede para calcular o menor tempo que Anne leva para sair do trabalho, pegar um ônibus e chegar à faculdade, considerando ruas com tempos diferentes e horários fixos de ônibus.

É um problema típico de **caminho mínimo em grafos com pesos positivos**, onde é necessário:
- Lidar com nomes de locais como vértices.
- Considerar restrições de tempo e lógica condicional no pós-processamento.
- Aplicar algoritmo de menor caminho com eficiência.

# Estratégia Utilizada

Foi usada uma lista de adjacência com dicionário, pois os vértices são nomes de lugares, e a fila de prioridade foi implementada com `heapq`, garantindo que os caminhos com menor tempo acumulado fossem processados primeiro.

A escolha do Dijkstra se deu pela necessidade de otimizar o tempo de deslocamento, já que outras técnicas como BFS simples ou DFS não consideram pesos. Podemos entender o Dijkstra como uma versão da BFS com prioridade, adaptada para trabalhar com grafos ponderados.

O algoritmo calcula o tempo de chegada baseado no caminho mais curto, e ainda verifica se Anne vai se atrasar dependendo do ônibus que ela pegar.


# Código

[Código](1977-icantbelate.py)

## Resultado

A lógica principal funcionou corretamente, mas a versão inicial apresentou erros de até **2 minutos nos testes finais**. Após algumas tentativas e ajustes no controle do tempo de embarque, a solução foi aceita.


---
