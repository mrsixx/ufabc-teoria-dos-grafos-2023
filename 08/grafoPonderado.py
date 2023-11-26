# Descrição: Faça um programa que faz a leitura de um grafo ponderado e imprime na tela as suas listas de adjacências com os pesos de cada arco.

# Entrada: Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um trio de inteiros, correspondentes ao início e fim do arco, seguido do peso do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída: Imprime as listas de adjacência com os pesos.

class Graph:
    def __init__(self, v, e):
        self._v = v
        self._e = e
        # crio a matriz de adjacencias para representar o grafo G = (V,E)
        # de modo que onde para u,v \in V, g[u][v] = 1 <-> (u,v) \in E (g[u][v] = 0 caso contrario)
        self._adj_matrix = [[0 for _ in range(v)] for _ in range(v)]

    def get_v(self):
        return self._v
    
    def get_e(self):
        return self._e


    def get_adj_matrix(self):
        return self._adj_matrix
    
    def get_adj_list(self):
        adj_list = []
        for tail_vertex, adjacencies in enumerate(self._adj_matrix):
            arrows = list(filter(lambda arrow: arrow[1] != 0, enumerate(adjacencies)))
            heads = list(map(lambda arrow: (arrow[0], arrow[1]), arrows))
            adj_list.append(heads)
        return adj_list
    
    def add_edge(self, u, v, w):
        if u < self._v and v < self._v:
            self._adj_matrix[u][v] = w

    def print_adj_list(self):
        for tail_vertex, adjacencies in enumerate(self.get_adj_list()):
            heads = list(map(lambda v: '%d(%d)' % (v[0], v[1]), adjacencies))
            print('%(vertex)d: %(incidencies)s' % {'vertex': tail_vertex, "incidencies": ' '.join(heads).strip()})

    def neighbours(self, v):
        if v is not None and v < self.get_v():
            return self.get_adj_list()[v]
        return []
    
    def has_edge(self, u,v):
        if u is None or u >= self.get_v():
            return False
        if v is None or v >= self.get_v():
            return False
        return bool(self.get_adj_matrix()[u][v])

    def transpose(self):
        v, e = self.get_v(), self.get_e()
        t = Graph(v,e)
        for i in range(v):
            for j in range(v):
                if g.has_edge(i,j):
                    t.add_edge(j,i)
        return t

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
    g.print_adj_list()