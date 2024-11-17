def solve_torreznos(test_cases):
    from heapq import heappop, heappush
    from collections import defaultdict

    def kruskal_mst(n, edges, banned_node=None):
        # Union-Find data structure
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            if root_x != root_y:
                if rank[root_x] > rank[root_y]:
                    parent[root_y] = root_x
                elif rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                else:
                    parent[root_y] = root_x
                    rank[root_x] += 1
                return True
            return False

        # Filter edges if banned_node is specified
        valid_edges = []
        for u, v, w in edges:
            if banned_node is not None and (u == banned_node or v == banned_node):
                continue
            valid_edges.append((w, u, v))

        # Sort edges by weight
        valid_edges.sort()

        mst_cost = 0
        mst_edges = 0

        # Perform Kruskal's algorithm
        for w, u, v in valid_edges:
            if union(u, v):
                mst_cost += w
                mst_edges += 1
                if mst_edges == n - 1:  # MST is complete
                    break

        return mst_cost

    results = []
    for n, m, f, s, edges in test_cases:
        # Compute the two MSTs
        cost_f_exclusive = kruskal_mst(n, edges, banned_node=s)
        cost_s_exclusive = kruskal_mst(n, edges, banned_node=f)
        results.append(cost_f_exclusive + cost_s_exclusive)
    return results

# Main function to handle input and output
def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    test_cases = []
    
    for _ in range(T):
        N, M, F, S = map(int, data[index].split())
        index += 1
        edges = []
        for __ in range(M):
            u, v, w = map(int, data[index].split())
            index += 1
            edges.append((u, v, w))
        test_cases.append((N, M, F, S, edges))
    
    results = solve_torreznos(test_cases)
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
