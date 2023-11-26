# Descrição: Faça um programa que implemente as operações com Conjuntos Disjuntos e imprima os resultados correspondentes.

# Entrada: Inicialmente, S é vazio.
# A primeira linha contém n, o total de operações com S.
# As linhas a seguir, temos n linhas, cada uma com uma operação:

# - findSet (S, x): devolve um representante de S_x.
# - makeSet (S, x): cria um novo conjunto com um único elemento x.
# - union (S, x, y): une dois conjuntos S_x e S_y.

# Saída: Imprime os resultados das operações com Conjuntos Disjuntos.
# Após cada operação "makeSet" ou "union", imprima o S resultante.
# Após cada operação "findSet" imprima o índice (representante) e S.

class DisjointSets:
    def __init__(self):
        self._sets = []
    
    def is_empty(self):
        return len(self._sets) == 0
    
    def find_set_idx(self, x):
        for i in range (len(self._sets)):
            for j in self._sets[i]:
                if j == x:
                    return i
        return -1
    
    def union(self, x, y):
        i = self.find_set_idx(x)
        j = self.find_set_idx(y)
        if i > -1 and j > -1:
            self._sets[i] += self._sets[j]
            self._sets[j].clear()


    def make_set(self, x):
        self._sets.append([x])

    def print(self):
        print(self._sets)


if __name__ == "__main__":
    n = int(input())
    S = DisjointSets()        
    for _ in range(n):
        entrada = list(tmp for tmp in input().split(" "))
        op = entrada[0]
        if op == 'M':
            S.make_set(entrada[1])
            S.print()
        elif op == 'F':
            idx = S.find_set_idx(entrada[1])
            print(idx, end=' ')
            S.print()
        elif op == 'U':
            S.union(entrada[1], entrada[2])
            S.print()