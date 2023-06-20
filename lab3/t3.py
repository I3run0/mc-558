class Node:    
    def __init__(self, indice=None, color=-1):
        self.indice = indice
        self.color = color

    def __repr__(self):
        return f"({self.indice}, {self.color})"
    
    def __str__(self):
        return f"({self.indice}, {self.color})"

def sortUtil(graph , i, visited, stack):
        visited[i] = True

        for element in graph[i]:
            if visited[element.indice] == False:

                sortUtil(graph, element.indice, visited, stack)

        stack.insert(0, i)

def topologicalSort(graph, n) -> list:
    visited = n * [False]
    stack = []

    for element in range(n):
        if visited[element] == False: 
            sortUtil(graph, element, visited, stack)

    return stack

def main():
    n, m, s, t = [int(i) for i in input().split()]

    graph = []
    out = n * [0]

    for _ in range(n):
        graph.append([])
        
    for _ in range(m):
        x, y, c = [int(i) for i in input().split(" ")]
        graph[x].append(Node(indice=y, color=c))
    

    topological_sort_stack = topologicalSort(graph=graph, n=n)
    topological_sort_stack.reverse()
    t_index = topological_sort_stack.index(t)

    yellow = n * [0]
    red = n * [0]
    green = n  * [0]
    green[t] = 1

    for i in range(t_index, n):
        for node in graph[topological_sort_stack[i]]:
            if node.indice == t or green[node.indice] + yellow[node.indice] + red[node.indice]:  
                if node.color == 0:     
                    green[topological_sort_stack[i]] += green[node.indice] + yellow[node.indice] + red[node.indice]
                
                elif node.color == 1:
                    yellow[topological_sort_stack[i]] += green[node.indice] + yellow[node.indice]
                
                elif node.color == 2:
                    red[topological_sort_stack[i]] += green[node.indice]
    
    for element in topological_sort_stack:
        out[element] = green[element] + yellow[element] + red[element]

    print(out[s])
    



if "__main__" == __name__:
    main()