from collections import deque

def bfs(G, visited, start, h):
    queue = deque([start])
    visited[start[0]][start[1]] = True
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(G) and 0 <= ny < len(G[0]) and not visited[nx][ny] and G[nx][ny] >= h:
                visited[nx][ny] = True
                queue.append((nx, ny))

def count_islands(G, h):
    visited = [[False for _ in range(len(G[0]))] for _ in range(len(G))]
    island_count = 0
    
    for i in range(len(G)):
        for j in range(len(G[0])):
            if G[i][j] >= h and not visited[i][j]:
                bfs(G, visited, (i, j), h)
                island_count += 1
                
    return island_count

def solve(N: int, M: int, G: list[list[int]]) -> int:
    """
    Return the maximum number of islands.

    N: number of rows
    M: number of columns
    G: grid of heights
    """
    max_islands = 0
    unique_heights = set()
    for row in G:
        unique_heights.update(row)
    
    for h in unique_heights:
        max_islands = max(max_islands, count_islands(G, h))
    
    return max_islands

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = [list(map(int, input().split())) for _ in range(N)]
        print(solve(N, M, G))

if __name__ == '__main__':
    main()