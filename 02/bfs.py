# Descrição: Faça um programa que faz a leitura de um grafo e imprime as distâncias obtidas a partir de um vértice s, de acordo com uma visita BFS (ou busca em largura).

# Entrada: Recebe n, m e s: n é o total de vértices, m o total de arcos e s o vértice inicial.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída: Imprime as distâncias obtidas a partir de s, pela busca BFS.

class Queue: 
    def __init__(self):
        self.array = []
    
    def enqueue(self, obj):
        self.array.append(obj)
    
    def dequeue(self):
        if self.is_empty():
            return None
        
        return self.array.pop(0)

    def is_empty(self):
        return len(self.array) == 0

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
            arrows = list(filter(lambda arrow: arrow[1] == 1, enumerate(adjacencies)))
            heads = list(map(lambda arrow: arrow[0], arrows))
            adj_list.append(heads)
        return adj_list
    
    def add_edge(self, u, v):
        if u < self._v and v < self._v:
            self._adj_matrix[u][v] = 1

    def print_adj_list(self):
        for tail_vertex, adjacencies in enumerate(self.get_adj_list()):
            heads = list(map(lambda v: str(v), adjacencies))
            print('%(vertex)distancies: %(incidencies)s' % {'vertex': tail_vertex, "incidencies": ' '.join(heads).strip()})

    def neighbours(self, v):
        if v is not None and v < self.get_v():
            return self.get_adj_list()[v]
        return []

def le_grafo(n,m): 
    g = Graph(n,m)
    for _ in range(m):
        # Para u,v \in V(g) leio o uv arco que está em E(g)
        u, v = (int(tmp) for tmp in input().split(" "))
        g.add_edge(u,v)
    return g

def bfs(g, s):
    distancies = [-1] * g.get_v()
    queue = Queue()
    queue.enqueue(s)
    distancies[s] = 0
    while not queue.is_empty():
        v = queue.dequeue()
        for n in g.neighbours(v):
            if distancies[n] != -1:
                continue
            distancies[n] = distancies[v] + 1
            queue.enqueue(n)
    return distancies

if __name__ == "__main__":
    n, m, s = (int(tmp) for tmp in input().split(" "))
    g = le_grafo(n, m)
    distancies = list(map(lambda d: str(d), bfs(g, s)))

    print('%(start)d: %(distancies)s' % {'start': s, "distancies": ' '.join(distancies).strip()})