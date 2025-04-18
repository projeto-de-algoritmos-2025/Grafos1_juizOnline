# Relatório  – Problema "O Rato no Labirinto" 

![rato_questao](../../assets/lista1/rato/questao.jfif)


![rato_questao_2](../../assets/lista1/rato/questao_2.jfif)

## Contextualização

O problema "O Rato no Labirinto", do Beecrowd tem como objetivo encontrar a quantidade mínima de pontos que um rato deve visitar para ir da **Entrada** até um ponto intermediário (**Queijo**, representado por `*`) e de lá até a **Saída**.

Trata-se de um problema clássico de busca em grafos, que exige:
- Leitura e construção correta de um grafo não-direcionado.
- Implementação de algoritmos de busca (como BFS) para encontrar caminhos mínimos.
- Respeito a detalhes do enunciado, como a contagem duplicada de nós em caminhos distintos.

 
 # Estratégia Utilizada

A solução proposta seguiu a seguinte abordagem:

1. Leitura da entrada e construção do grafo usando estrutura de listas de adjacência.
2. Busca em largura BFS para encontrar o caminho mais curto.
3. Contagem do total de nós visitados, somando os tamanhos dos dois caminhos (permitindo a contagem duplicada do `*` (queijo), conforme o enunciado exige).

# Codigo

[Código](rato_labirinto_bfs.py)

## Resultado

A implementação submetida foi capaz de **resolver corretamente aproximadamente 60% dos casos de teste**, 
Apesar do esforço dedicado, o projeto alcançou uma taxa de acerto parcial. Testes adicionais no Beecrowd apresentaram falhas por **diferenças de apenas 1 ou 2 unidades**, indicando que casos específicos geraram erros

![solucao_rato](../../assets/lista1/rato/resultado.jfif)