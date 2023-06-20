FATHER, RANK = [], []

def init_structs(n: int):
    for _ in range(n):
        FATHER.append(0)
        RANK.append(0)

    for i in range(n):    
        FATHER[i] = i
        RANK[i] = 0

def find_set(x: int) -> int:
    if x != FATHER[x]:
        FATHER[x] = find_set(FATHER[x])
    return FATHER[x]

def link(x: int, y: int):
    if RANK[x] > RANK[y]:
        FATHER[y] = x
    else:
        FATHER[x] = y

        if RANK[x] == RANK[y]:
            RANK[y] == RANK[y] + 1

def union(x, y):
    link(find_set(x), find_set(y))

def main():
    n, m, k = [int(i) for i in input().split(" ")]
    
    edges, solution = [], []
    
    init_structs(n)

    for i in range(m):
        a, b, w = [int(j) for j in input().split(" ")]
        edges.append((w, a, b))
 
    edges.sort()
    
    for i in range(m):
        if find_set(edges[i][1]) != find_set(edges[i][2]):
            solution.append(edges[i][0])
            union(edges[i][1], edges[i][2])
            n -= 1

            if n == k: 
                break
    
    print(sum(solution))



if "__main__" == __name__:
    main()