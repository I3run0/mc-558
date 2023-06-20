class Node:    
    def __init__(self, next=None, my_addresss=None, indice=0, color=-1, visited=0):
        self.next = next
        self.my_address = my_addresss
        self.indice = indice
        self.color = color
        self.visited = visited

    def __repr__(self):
        return f"{self.indice}, {None if self.next == None else self.next.indice}, {self.color}, {self.visited}"
    
    def __str__(self):
        return f"{self.indice}, {None if self.next == None else self.next.indice}, {self.color}, {self.visited}"

class Queue:
    head: Node()
    tail: Node()

    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def is_empty(self) -> bool:
        return self.head == None and self.tail == None
    
    def __str_format(self):
        iterator = self.head
        out = "["
        
        while(iterator != None):
            out += "[" + str(iterator) + "],"
            iterator = iterator.next
        out += "]"
        return out 
    
    def __repr__(self):
        return self.__str_format()
    
    def __str__(self):
        return self.__str_format()
    
def insert_queue(queue: Queue, next_node: Node):
    if queue.is_empty():
        queue.head = next_node
        queue.tail = next_node
        return
    
    queue.tail.next = next_node
    queue.tail = next_node

def make_graph(n):
    out = []
    for _ in range(n):
        out.append(Queue())
    
    return out


def maximal_trail(r, adj, color):
    u = r
    T = [r]
    color = color
    v = adj[u].head
    while v != None: 
        next = 0
        c = 0
        if (color == None or color != v.color) and v.visited == 0: 
            print(u, v.indice)
            c = v.color
            u = v.indice
            T.append(u)
            v.visited = 1
            v.my_address.visited = 1
            next = k = adj[u].head
            
        
        v = v.next if next == 0 else next
        color = color if next == 0 else c
    return (T, color)

def main():
    n, m = [int(i) for i in input().split(" ")]

    graph = make_graph(n)
    
    for _ in range(m):
        u, v, c = [int(j) for j in input().split(" ")]
        color = True if c == 0 else False
        vert_v = Node(None, None, v, color, 0)
        vert_u = Node(None, vert_v, u, color, 0)
        vert_v.my_address = vert_u
        insert_queue(graph[u], vert_v)
        insert_queue(graph[v], vert_u)
        
    T, color = maximal_trail(0, graph, None)
    
    while True:
        found = False
        t , s = (0, 0)
        idx = 0
        while t < len(T) and not(found):
            v = graph[T[t]].head
            V = graph[T[t]].head
            while(v != None):
                if color != v.color and v.visited == 0:
                    found = True
                    s = T[t]
                    print(f"Vertice a ser escolhido {T[t]}")
                    break
                v = v.next
            t += 1
        
        print(T)
        if not(found):
            break

        new_t, color = maximal_trail(s, graph, color)
        T = T[:t - 1] + new_t + T[t:]

    print(len(T))
    if T[0] == T[len(T) - 1]:
        for i in range(len(T)):
            if i + 1 == len(T):
                print(f'{T[i]}')
            else:
                print(f'{T[i]}', end=" ")
    else:
        print("Não possui trilha Euleriana alternante")
    

if "__main__" == __name__:
    main()