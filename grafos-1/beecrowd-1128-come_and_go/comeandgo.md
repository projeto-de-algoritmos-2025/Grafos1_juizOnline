# Relatório – Problema "Come and Go" (Beecrowd 1128)

![questao_comeandgo](../../assets/lista1/come_1128/comeandgo.png)

![codigo_comeandgo](../../assets/lista1/come_1128/codigo-comeandgo.png)

## Contextualização

A questão "Come and Go", do Beecrowd, tem como objetivo verificar se é possível ir e voltar entre quaisquer duas cidades de um mapa com ruas direcionadas (mão única ou dupla). O problema é um caso clássico de verificação de **grafo fortemente conexo**.

Ele exige:
- Leitura adequada de grafos direcionados.
- Tratamento específico para ruas de mão dupla.
- Aplicação de algoritmos de busca em profundidade (DFS) para análise de conectividade.

# Estratégia Utilizada

Considerando que as ruas podem ser de mão única ou dupla, utilizei grafos fortemente conexos.

Escolhi usar duas buscas em profundidade (DFS), uma no grafo original e outra no grafo transposto com as direções invertidas. Se ambas alcançarem todos os vértices, então o grafo é considerado fortemente conexo.

Representamos o grafo com listas de adjacência, por ser mais leve e apropriada para o número de vértices e operações de vizinhança.


# Código

[Código](1128-comeandgo.py)

## Resultado

Após os ajustes e revisão, a solução obteve sucesso nos testes do Beecrowd.  
A lógica foi validada por meio da dupla DFS e passou corretamente em **100% dos casos de teste**.

---
