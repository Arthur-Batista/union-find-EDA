# Estrutura de Dados Union-Find (Conjuntos Disjuntos)

Este projeto apresenta uma implementação da estrutura de dados Union-Find (também conhecida como Disjoint-Set), com diferentes otimizações e análises de complexidade.

## Visão Geral

A estrutura Union-Find é uma ferramenta fundamental para lidar com coleções de conjuntos dinâmicos disjuntos. Ela permite realizar duas operações principais de forma eficiente:

*   **FIND-SET(x):** Encontrar o conjunto ao qual um elemento *x* pertence.
*   **UNION(x, y):** Unir os conjuntos que contêm os elementos *x* e *y*.

Este projeto explora diferentes implementações da estrutura Union-Find, incluindo:

*   Listas Ligadas (com e sem a heurística de união ponderada)
*   Florestas de Conjuntos Disjuntos (árvores enraizadas) com as heurísticas de união por rank e compressão de caminho

Além das implementações, o projeto também analisa a complexidade de tempo de cada abordagem e discute suas aplicações práticas.

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

*   `unionFindLinkedList.py`: Implementação da estrutura Union-Find com listas ligadas (com e sem união ponderada).
*   `unionFindTree.py`: Implementação da estrutura Union-Find com florestas de conjuntos disjuntos (união por rank e compressão de caminho).

## Execução Remota no Google Colab

Você pode experimentar e rodar o código deste projeto diretamente no Google Colab utilizando os seguintes links:

*   **Florestas de Conjuntos Disjuntos:** [https://colab.research.google.com/drive/1DNFQI2MKo1Ym1pj2XiC2UVJpU5iMG_iv](https://colab.research.google.com/drive/1DNFQI2MKo1Ym1pj2XiC2UVJpU5iMG_iv)
*   **Listas Ligadas:** [https://colab.research.google.com/drive/10EzxjXMcNn82u6P8s4NSkbZZScBu9DHA](https://colab.research.google.com/drive/10EzxjXMcNn82u6P8s4NSkbZZScBu9DHA)

## Slides Utilizados para apresentação

Os slides utilizados para a implementação e análise da estrutura Union-Find pode ser encontrado [neste arquivo PDF](Trabalho_EDA.pdf).

## Aplicações

A estrutura de dados Union-Find pode ser utilizada em diversas aplicações, incluindo:

*   Determinação das componentes conexas de um grafo
*   Algoritmo de Kruskal para encontrar a árvore geradora mínima de um grafo
*   Detecção de ciclos em grafos
*   Agrupamento (clustering)

## Equipe

*   Arthur Batista
*   Malu Brito
*   Tiago Almeida

## Referências

*   CORMEN, Thomas. *Algoritmos – Teoria e Prática*. 3.ed. Rio de Janeiro: LTC, 2022.
