# Descrição: Faça um programa que faz a leitura de um grafo e imprime na tela as suas listas de adjacências.

# Entrada: Recebe n e m; n é o total de vértices e m o total de arcos.
# A seguir, m linhas, cada linha com um par de inteiros, correspondentes ao início e fim do arco.
# (Os vértices são identificados de 0 até n-1.)

# Saída: Imprime as listas de adjacência.

def le_grafo(): 
    # leitura dos inteiros que parametrizam o total de vertices e o total de arcos
    n, m = (int(tmp) for tmp in input().split(" "))
    # crio a matriz de adjacencias para representar o grafo G = (V,E)
    # de modo que onde para u,v \in V, g[u][v] = 1 <-> (u,v) \in E (g[u][v] = 0 caso contrario)
    g = [[0 for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        # Para u,v \in V(g) leio o uv arco que está em E(g)
        u, v = (int(tmp) for tmp in input().split(" "))
        if u < n and v < n:
            g[u][v] = 1
    return g


def imprime_lista_adjacencias(g):
    for tail_vertex, adjacencies in enumerate(g):
        arrows = list(filter(lambda arrow: arrow[1] == 1, enumerate(adjacencies)))
        heads = list(map(lambda arrow: '%s' % arrow[0], arrows))
        print('%(vertex)d: %(incidencies)s' % {'vertex': tail_vertex, "incidencies": ' '.join(heads).strip()})

if __name__ == "__main__":
    g = le_grafo()
    imprime_lista_adjacencias(g)