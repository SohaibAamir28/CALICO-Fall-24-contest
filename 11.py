import heapq

def find_minimum_cost(N: int, M: int, F: int, S: int, roads: list) -> int:
    # Initialize adjacency list
    graph = [[] for _ in range(N)]
    for u, v, w in roads:
        graph[u].append((v, w))
        graph[v].append((u, w))

    def dijkstra(start, blocked):
        min_heap = [(0, start)]
        dist = [float('inf')] * N
        dist[start] = 0
        visited = [False] * N

        while min_heap:
            current_dist, u = heapq.heappop(min_heap)

            if visited[u]:
                continue

            visited[u] = True

            for v, weight in graph[u]:
                if v == blocked:
                    continue
                if current_dist + weight < dist[v]:
                    dist[v] = current_dist + weight
                    heapq.heappush(min_heap, (dist[v], v))

        return dist

    # Run Dijkstra from France, blocking Spain
    dist_from_france = dijkstra(F, S)
    # Run Dijkstra from Spain, blocking France
    dist_from_spain = dijkstra(S, F)

    # Calculate the minimum cost to connect all countries without passing through the blocked country
    total_cost = 0
    for i in range(N):
        if i != F and i != S:
            total_cost += min(dist_from_france[i], dist_from_spain[i])

    return total_cost

def main():
    T = int(input())
    for _ in range(T):
        N, M, F, S = map(int, input().split())
        roads = [tuple(map(int, input().split())) for _ in range(M)]
        print(find_minimum_cost(N, M, F, S, roads))

if __name__ == '__main__':
    main()