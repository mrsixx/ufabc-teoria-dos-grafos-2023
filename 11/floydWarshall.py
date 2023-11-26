import numpy as np
# Descrição: Faça um programa que faz a leitura de um grafo ponderado.
# O programa deve imprimir na tela a matriz de distâncias e a matriz "PI" dos caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

# Entrada: Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída: Imprime as distâncias e os caminhos mínimos obtidos pelo algoritmo de Floyd-Warshall.

class Graph:
    def __init__(self, v, e):
        self._v = v
        self._e = e
        # crio a matriz de adjacencias para representar o grafo G = (V,E)
        # de modo que onde para u,v \in V, g[u][v] = 1 <-> (u,v) \in E (g[u][v] = 0 caso contrario)
        self._adj_matrix = np.matrix([[0 for _ in range(v)] for _ in range(v)])
        self._dist_matrix = np.matrix([[(np.Inf if i != j else 0) for j in range(v)] for i in range(v)])
        self._pred_matrix = np.matrix([[-1 for _ in range(v)] for _ in range(v)])
        

    def get_v(self):
        return self._v
    
    def get_e(self):
        return self._e

    def get_adj_matrix(self):
        return self._adj_matrix
    
    def get_dist_matrix(self):
        return self._dist_matrix

    def get_pred_matrix(self):
        return self._pred_matrix

    def add_edge(self, u, v, w):
        if u < self._v and v < self._v:
            self._adj_matrix[u,v] = w

    def has_edge(self, u,v):
        if u is None or u >= self.get_v():
            return False
        if v is None or v >= self.get_v():
            return False
        return self.get_adj_matrix()[u,v] != 0
    
    def min(self, a, b):
        if a != np.Inf and b != np.Inf:
            return int(0.5 *(a + b - abs(a - b)))
        
        if a == np.Inf:
            return b
        return a
    
    def initialize_dist_matrix(self):
        n = self.get_v()
        for u in range(n):
            for v in range(n):
                if self.has_edge(u,v):
                    self.get_dist_matrix()[u,v] = self.get_adj_matrix()[u,v]

    def initialize_pred_matrix(self):
        n = self.get_v()
        for u in range(n):
            for v in range(n):
                if self.has_edge(u,v):
                    self.get_pred_matrix()[u,v] = u

    def floyd_warshall(self):
        n = self.get_v()
        for k in range(n):
            d_k1 = self.get_dist_matrix().copy()
            pi_k1 = self.get_pred_matrix().copy()
            for i in range(n):
                for j in range(n):
                    if d_k1[i,j] <= d_k1[i,k] + d_k1[k,j]:
                        self.get_pred_matrix()[i,j] = pi_k1[i,j]
                    else:
                        self.get_pred_matrix()[i,j] = pi_k1[k,j]
                    self.get_dist_matrix()[i,j] = self.min(d_k1[i,j], d_k1[i,k] + d_k1[k,j])

    
def le_grafo(n,m):
    g = Graph(n,m)
    for _ in range(m):
        # Para u,v \in V(g) leio o uv arco que está em E(g)
        u, v, w = (int(tmp) for tmp in input().split(" "))
        g.add_edge(u,v,w)
    return g


if __name__ == "__main__":
    n, m = (int(tmp) for tmp in input().split(" "))
    g = le_grafo(n, m)

    g.initialize_dist_matrix()
    g.initialize_pred_matrix()

    g.floyd_warshall()
    print(g.get_dist_matrix().astype(int))
    print(g.get_pred_matrix().astype(int))