# Descrição: Faça um programa que faz a leitura de um grafo e imprime a expressão de parênteses dos componentes fortemente conexos.

# Entrada: Recebe n, m: n é o total de vértices, m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída: Imprime a expressão de parênteses dos componentes fortemente conexos.

class Stack: 
    def __init__(self):
        self.array = []
    
    def push(self, obj):
        self.array.append(obj)
    
    def pop(self):
        if self.is_empty():
            return None
        
        return self.array.pop()
    
    def peek(self):
        if self.is_empty():
            return None
        
        return self.array[-1]

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
        u, v = (int(tmp) for tmp in input().split(" "))
        g.add_edge(u,v)
    return g


def dfs(g, sorted_vertex_list=None):
    stacked = [-1] * g.get_v()
    unstacked = [-1] * g.get_v()
    if sorted_vertex_list is None:
        sorted_vertex_list = range(g.get_v())
    t = 0
    for v in sorted_vertex_list:
        if stacked[v] != -1:
            continue
        t = t+1
        stack = Stack()
        stack.push(v)
        stacked[v] = t

        while not stack.is_empty():
            t = t+1
            v = stack.peek()
            unknown_neighbours = list(filter(lambda n: stacked[n] == -1, g.neighbours(v)))
            if len(unknown_neighbours) > 0:
                next = unknown_neighbours[0]
                stacked[next] = t
                stack.push(next)
            else:
                unstacked[v] = t
                stack.pop()            

    return stacked, unstacked

def index_of(el, lst):
    try:
        return lst.index(el)
    except:
        return -1
        
def by_unstack_time(k):
    return k[1]

def calc_parentheses_expression(g):
    instants = []
    stacked, unstacked = dfs(g)
    dec_unstacked_vertex = [v[0] for v in sorted(enumerate(unstacked),key=by_unstack_time, reverse=True)]
    tstacked, tunstacked = dfs(g.transpose(), dec_unstacked_vertex)
    print()
    # todo vértice aparece 2x na expressão
    for t in range(2 * g.get_v()):
        tl = t+1
        stacked_vertex = index_of(tl, tstacked)
        unstacked_vertex = index_of(tl, tunstacked)

        if stacked_vertex != -1:
            instants.append('_(%d_' % stacked_vertex)
        elif unstacked_vertex != -1:
            instants.append('_%d)_' % unstacked_vertex)
    return ''.join(instants).replace('__', '_').replace('_', ' ').strip()

if __name__ == "__main__":
    n, m = (int(tmp) for tmp in input().split(" "))
    g = le_grafo(n, m)
    print(calc_parentheses_expression(g))