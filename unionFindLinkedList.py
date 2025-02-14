class Node:
    def __init__(self, representante, tamanho):
        self.representante = representante
        self.tamanho = tamanho
        self.cabeca = self
        self.cauda = self
        self.proximo = None

class UnionFind:
    def __init__(self):
        self.sets = {}  # Dicionário para armazenar os conjuntos (Node)

    def makeset(self, x):
        node = Node(x, 1)
        self.sets[x] = node
    
    def findset(self, x):
        return self.sets[x].representante
    
    def union(self, x, y):
        X = self.sets[self.findset(x)]
        Y = self.sets[self.findset(y)]
        if X.representante == Y.representante:
          return
        
        if X.tamanho < Y.tamanho:
            current = X.cabeca
            while current is not None:
                current.representante = Y.representante
                current = current.proximo
            Y.tamanho = X.tamanho + Y.tamanho
            X.tamanho = 0
            Y.cauda.proximo = X.cabeca
            Y.cauda = X.cauda
            X.cabeca = None
        else:
            current = Y.cabeca
            while current is not None:
                current.representante = X.representante
                current = current.proximo
            X.tamanho = X.tamanho + Y.tamanho
            Y.tamanho = 0
            X.cauda.proximo = Y.cabeca
            X.cauda = Y.cauda
            Y.cabeca = None

# Exemplo de uso:
uf = UnionFind()
uf.makeset(1)
uf.makeset(2)
uf.makeset(3)
print(uf.findset(1)) #1
print(uf.findset(2)) #2
uf.union(1,2)
print(uf.findset(1)) #1
print(uf.findset(2)) #1
print(uf.findset(3)) #3
uf.union(1,3)
print(uf.findset(1)) #1
print(uf.findset(2)) #1
print(uf.findset(3)) #1