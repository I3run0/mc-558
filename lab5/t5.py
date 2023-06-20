INFINITY = float("inf")

def bellman_ford(edges: list, w: list, s: int, n: int, energy: int):
    d = []

    for _ in range(n):
        d.append(INFINITY)
    
    d[s] = 0

    for i in range(n - 1):
        for j in range(len(edges)):
            if d[edges[j][0]] + w[edges[j][1]] < energy and \
                    d[edges[j][1]] > d[edges[j][0]] + w[edges[j][1]]:
                d[edges[j][1]] = d[edges[j][0]] + w[edges[j][1]]
            
    return d

def main():
    n = int(input())
    w = [-1 * int(i) for i in input().split(" ")]
    m = int(input())

    energy = 100 
    edges = []

    for _ in range(m):
        u, v = [int(i) for i in input().split(" ")]
        edges.append((u, v))
    
    d = bellman_ford(edges, w, 0, n, energy)
    
    if d[n - 1] == INFINITY:
        print("impossible")
    else:
        print("possible")

if __name__ == "__main__":
    main()