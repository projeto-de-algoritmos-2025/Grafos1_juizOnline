# Relatório de Implementação – Problema "Minha Camiseta Me Serve" (Beecrowd 1362)

![camisa_favorita_questao](../../assets/lista1/camisa/questao.jfif)



## Contextualização

O problema "Minha Camiseta Me Serve", do Beecrowd , consiste em verificar se é possível distribuir `N` camisetas entre `M` voluntários, de modo que:

- Cada voluntário receba exatamente uma camiseta.
- Cada camiseta seja utilizada por no máximo um voluntário.
- Cada voluntário aceita apenas dois tamanhos de camiseta entre: `XS, S, M, L, XL, XXL`.
- As camisetas estão disponíveis em quantidades iguais por tamanho: `N / 6`.

Trata-se de um problema de matching em grafo bipartido, que exige:
- Modelagem adequada de voluntários e camisetas como vértices bipartidos.
- Algoritmo de emparelhamento com realocação recursiva (DFS com backtracking).
- Controle rigoroso do estado de camisetas ocupadas e caminhos válidos.


## Estratégia Utilizada

A solução implementada seguiu os seguintes passos:

1. Mapeamento de tamanhos (`XS` a `XXL`) para índices de 0 a 5.
2. Geração de camisetas individuais com IDs únicos, respeitando a quantidade de cada tamanho.
3. Construção do grafo bipartido, onde cada voluntário é conectado às camisetas dos dois tamanhos que aceita.
4. Algoritmo de busca em profundidade (DFS) para tentar alocar cada voluntário a uma camiseta:
   - Se a camiseta estiver livre, alocamos.
   - Se estiver ocupada, tentamos realocar quem está usando ela (chamada recursiva).
5. Controle com o vetor `visitado` para evitar loops e repetição na mesma rodada de DFS.
6. Verificação final se foi possível atender todos os `M` voluntários.


# Código

[Código](camisa_favorita_biparticao.py)


## Resultado

A implementação foi um sucesso pois passou em todos os casos de uso

![camisa_favorita_resultado](../../assets/lista1/camisa/resultado.jfif)