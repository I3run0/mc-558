class Node:
    degre: int
    node_index: int

    def __init__(self, degre: int, node_index: int):
        self.degre = degre
        self.node_index = node_index
    
    def __radd__(self, other):
        return self.degre + other

    def __ls__(self, other):
        return self.degre < other.degre

    def __gt__(self, other):
        return self.degre > other.degre

    def __repr__(self):
        return f'[{self.degre}, {self.node_index}]'

    def __str__(self):
        return f'[{self.degre}, {self.node_index}]'
        
def make_graph(n: int):
    graph = dict()

    for i in range(1, n + 1):
        graph[i] = []

    return graph

def make_degre_list(n: int):
    degre_list = list()
    degres = input().split(" ")
    for i in range(1, n + 1):
        degre_list.append(Node(int(degres[i - 1]), i))

    return degre_list

def solve_graph_sequence(degre_list: list, graph: dict):
    
    if not(len(degre_list) > 0):
        return False

    if sum(degre_list) % 2 != 0 or degre_list[0].degre > len(degre_list):
        return False
    
    pivot_degre = degre_list.pop(0)

    for i in range(pivot_degre.degre):
        degre_list[i].degre -= 1
        
        graph[degre_list[i].node_index].append(pivot_degre.node_index)
        graph[pivot_degre.node_index].append(degre_list[i].node_index)

    degre_list.sort()

    while len(degre_list) > 0 and degre_list[len(degre_list) - 1].degre == 0:
        degre_list.pop(len(degre_list) - 1)

    if not(solve_graph_sequence(degre_list, graph)):
        return False
    
    return True

def print_graph(graph: dict):
    for i in graph.keys():
        out = " ".join([str(i) for i in graph[i]])
        print(out)

def main():
    n = int(input())
    graph = make_graph(n)
    degre_list = make_degre_list(n)
    solve_graph_sequence(degre_list, graph)
    print_graph(graph)

if "__main__" == __name__:
    main()
