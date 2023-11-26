# Descrição: Faça um programa que implemente uma fila de prioridade e imprima na tela os resultados das operações especificadas na entrada.

# Entrada: Na primeira linha, o programa recebe dois inteiros n e k: n é o tamanho da fila, k é a quantidade de operações.
# Inicialmente, a fila Q está vazia, ou seja, Q = [0] * n.
# Na segunda linha, temos n chaves.
# A partir da terceira linha, temos k operações, uma operação por linha.

# Cada operação pode ser:

# - vazio (Q): devolve True se fila vazia, False caso contrário.
# - insere (Q, i): insere o índice i na fila Q, ou seja, faz Q[i] = 1.
# - busca (Q, i): devolve 1 se o índice i estiver na fila, 0 caso contrário (ou seja, devolve Q[i]).
# - extraiMinimo (Q): remove e devolve o índice de Q com a menor chave.
# - minimo (Q): devolve o índice de Q com a menor chave (sem remover).

# Saída: Imprime os resultados das operações com a fila de prioridade.
# Após cada operação "insere", imprima a fila resultante.
# Após "extraiMinimo", imprima o elemento removido e a fila resultante. 
# Após "minimo", imprima o elemento devolvido e a fila resultante.
# Após "busca" ou "vazio", imprima o resultado e a fila.

class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.min_heap = [0] * capacity
        self.tail_idx = -1
    
    def is_empty(self):
        return self.tail_idx == -1
    
    def get_left_idx(self, idx):
        return (2 * idx) + 1
    
    def get_right_idx(self, idx):
        return 2 * (idx + 1)

    def get_parent_idx(self, idx):
        return (idx-1) // 2

    def print(self):
        print(self.min_heap)

    def insert(self, key):
        if self.tail_idx >= len(self.min_heap) -1 :
            raise Exception('Capacidade da fila estourada.')
        
        self.tail_idx += 1
        self.min_heap[self.tail_idx] = key
        i = self.tail_idx
        while i > 0 and self.min_heap[self.get_parent_idx(i)] < self.min_heap[i]:
            swap = self.min_heap[i]
            self.min_heap[i] = self.min_heap[self.get_parent_idx(i)]
            self.min_heap[self.get_parent_idx(i)] = swap
            i = self.get_parent_idx(i)

    def dequeue(self):
        if self.is_empty():
            raise Exception('empty')
        min = self.min_heap[0]
        self.min_heap[0] = self.min_heap[self.tail_idx]
        self.tail_idx -= 1
        self.heapify(0)
        return min

    def heapify(self, index):
        if self.is_leaf(index) or not self.isValidIndex(index):
            pass
        
        max_idx = self.max_index(index, self.get_left_idx(index), self.get_right_idx(index))

        if max_idx != index:
            self.swap(index, max_idx)
            self.heapify(max_idx)

    def contains(self, key):
        return True

if __name__ == "__main__":
    n, k = (int(tmp) for tmp in input().split(" "))
    q = PriorityQueue(n)
    for key in (int(tmp) for tmp in input().split(" ")):
        q.insert(key)
        
    for _ in range(k):
        x = list(tmp for tmp in input().split(" "))
        op = x[0]
        if(len(x) > 1):
            param = x[1]
            if op == 'I':
                q.print()
            elif op == 'B':
                print(q.contains(param), q.min_heap)
        else:
            if op == 'M':
                print(q.min_heap[0], q.min_heap)
            elif op == 'E':
                print(q.dequeue(), q.min_heap)
            elif op == 'V':
                print(q.is_empty(), q.min_heap)