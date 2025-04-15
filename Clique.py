from collections import defaultdict

def clique(grid: list[list[int]]) -> int:
    ln = len(grid)
    a,a1 = [],1
    for i in range(1,ln+1):
        for j in range(1,ln+1):
            if not grid[i-1][j-1]:
                a.append((i,j,a1))
                a1+=1
    if not a:
        return ln
    b = defaultdict(set)
    for i,j,m in a:
        b[i].add(m)
        b[j].add(m)
    c = [{j for j in range(1,a1)}-b[i] for i in range(1,ln+1)]
    ecx = 1
    state = True
    while state:
        for i in range(0,ln):
            d = c[i] 
            if not d:
                state=False
                break
            for j in range(1,ln+1):
                e = c[i]-b[j]
                if len(e) < len(d):
                    d = e
            c[i] = d
        if state:
            ecx += 1
    return ln-ecx

def main() -> int:
    edges = {
    1:(2,3,4),
    2:(1,3,5,13,14),
    3:(1,2,4,5,13),
    4:(1,3,5,6,8,9),
    5:(2,3,4,6,7,12,13),
    6:(4,5,7,8,10,11),
    7:(5,6,8,10,11,12),
    8:(4,6,7,11,10,9),
    9:(4,8,10),
    10:(9,8,6,7,11,21),
    11:(7,6,8,10,21,12,15,12),
    12:(7,13,5,15,11,16),
    13:(2,3,5,12,16,14),
    14:(2,13,16),
    15:(16,17,19,18,11,12),
    16:(12,13,14,15,17),
    17:(16,15,19),
    18:(11,15,19,20,21),
    19:(17,15,18,20),
    20:(21,18,19),
    21:(10,11,18,20)
    }
    numberofvertex = 21
    grid = [[0 for _ in range(numberofvertex)] for _ in range(numberofvertex)]
    for i in range(1,numberofvertex):
        grid[i-1][i-1] = 1
        if i not in edges:
            continue
        for j in edges[i]:
            grid[i-1][j-1] = 1
    max_clique = clique(grid)
    print(max_clique)
    return 0
main()
