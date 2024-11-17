from collections import deque
import heapq

def solve(N: int, M: int, K: int, C: list[str]) -> int:
    """
    Perform BFS with priority queue (Dijkstra-like) to find the shortest path
    from S to E in the grid. Returns the minimum number of moves or -1 if 
    reaching E is impossible.
    """
    # Locate the start (S) and end (E) positions
    start = end = None
    for i in range(N):
        for j in range(M):
            if C[i][j] == 'S':
                start = (i, j)
            elif C[i][j] == 'E':
                end = (i, j)

    if not start or not end:
        return -1  # Invalid grid (no start or end)

    # Directions for walking/dashing
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Priority queue and visited set
    pq = [(0, start[0], start[1], True)]  # (moves, x, y, can_dash)
    visited = set([(start[0], start[1], True)])

    while pq:
        moves, x, y, can_dash = heapq.heappop(pq)

        # If we reach the end exactly
        if (x, y) == end:
            return moves

        # Walking to adjacent tiles
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and C[nx][ny] != '#' and (nx, ny, can_dash) not in visited:
                visited.add((nx, ny, can_dash))
                heapq.heappush(pq, (moves + 1, nx, ny, can_dash))

        # Dashing if possible
        if can_dash:
            for dx, dy in directions:
                for step in range(1, K + 1):
                    nx, ny = x + step * dx, y + step * dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if C[nx][ny] == '#':
                            break  # Stop at walls
                        new_can_dash = C[nx][ny] == '*'  # Reset dash if hitting a crystal
                        # Stop dashing exactly on E or valid tiles
                        if (nx, ny) == end:
                            heapq.heappush(pq, (moves + 1, nx, ny, False))
                            visited.add((nx, ny, False))
                            break
                        if (nx, ny, new_can_dash) not in visited:
                            visited.add((nx, ny, new_can_dash))
                            heapq.heappush(pq, (moves + 1, nx, ny, new_can_dash))
                    else:
                        break  # Stop at grid boundaries

    # If we exhaust the queue without finding the end
    return -1


def main():
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        C = [input().strip() for _ in range(N)]
        print(solve(N, M, K, C))


if __name__ == '__main__':
    main()
