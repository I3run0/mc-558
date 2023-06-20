class Node:
    def __init__(self, index):
        self.index = index
        self.visited = False

def make_graph(n: int ):
    graph = []

    for i in range(n):
        graph.append(Node(i))

    return graph

def euler_solve(g):



def main():
    n, m = [int(i) for i in input().split(" ")]

    graph = make_graph(n)
    e = set()

    for _ in range(m):
        u, v, c = [int(j) for j in input().split(" ")]
        e.add((u, v))
        graph[u].append(graph[v])
        graph[v].append(graph[u])

    euler_solve(graph)




if "__main__" == __name__:
    main()