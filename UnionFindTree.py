class UnionFindTree:  # Union-Find com Árvores (Apenas)
    def __init__(self, n):
        """
        Inicializa a estrutura Union-Find com 'n' elementos.
        Cada elemento começa como um conjunto individual.
        """
        self.parent = list(range(n))  # Inicialmente, cada nó é seu próprio pai
        self.rank = [0] * n  # Rank inicial de cada nó é 0 (usado para Union by Rank)

    def find(self, x):
        """
        Encontra o representante (raiz) do conjunto ao qual o elemento 'x' pertence.
        Aplica 'path compression' para otimizar futuras buscas.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Compressão de Caminho
        return self.parent[x]

    def union(self, x, y):
        """
        Une os conjuntos que contêm os elementos 'x' e 'y'.
        Usa 'union by rank' para manter as árvores balanceadas.
        """
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:  # Se os elementos estão em conjuntos diferentes
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y  # Anexa a árvore de menor rank à de maior rank
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x  # Se os ranks são iguais, anexa e incrementa o rank
                self.rank[root_x] += 1


# Exemplos de Uso:
print("Exemplo com Árvores (Implementação Única):")
uf_tree = UnionFindTree(10)  # Cria 10 conjuntos: 0, 1, 2, ..., 9

# Verificar representantes iniciais
for i in range(10):
    print(f"Representante de {i}: {uf_tree.find(i)}")

# Unir alguns conjuntos
uf_tree.union(0, 1)
uf_tree.union(2, 3)
uf_tree.union(1, 3)  # Unir conjuntos que já foram unidos
uf_tree.union(4, 5)
uf_tree.union(6, 7)
uf_tree.union(8, 9)
uf_tree.union(6, 8)

# Verificar representantes após as uniões
print("\nRepresentantes após as uniões:")
for i in range(10):
    print(f"Representante de {i}: {uf_tree.find(i)}")

# Verificar se alguns elementos estão no mesmo conjunto
print("\nVerificando se alguns elementos estão no mesmo conjunto:")
print(f"0 e 1 estão no mesmo conjunto? {uf_tree.find(0) == uf_tree.find(1)}")  # True
print(f"2 e 3 estão no mesmo conjunto? {uf_tree.find(2) == uf_tree.find(3)}")  # True
print(f"0 e 2 estão no mesmo conjunto? {uf_tree.find(0) == uf_tree.find(2)}")  # True
print(f"4 e 5 estão no mesmo conjunto? {uf_tree.find(4) == uf_tree.find(5)}")  # True
print(f"6 e 8 estão no mesmo conjunto? {uf_tree.find(6) == uf_tree.find(8)}")  # True
print(f"0 e 5 estão no mesmo conjunto? {uf_tree.find(0) == uf_tree.find(5)}")  # False