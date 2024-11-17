# celeste_solver.py

from collections import deque

def solve(N: int, M: int, K: int, grid: list[str]) -> int:
    # Locate start (S) and end (E) positions
    start = end = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'E':
                end = (i, j)

    if not start or not end:
        return -1  # Invalid grid (no start or end)

    # BFS Initialization
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    queue = deque([(start[0], start[1], True, 0)])  # (x, y, can_dash, moves)
    visited = set([(start[0], start[1], True)])  # Track visited states

    while queue:
        x, y, can_dash, moves = queue.popleft()

        # Check if we reached the end
        if (x, y) == end:
            return moves

        # Walk to adjacent tiles
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#' and (nx, ny, can_dash) not in visited:
                visited.add((nx, ny, can_dash))
                queue.append((nx, ny, can_dash, moves + 1))

        # Dash if possible
        if can_dash:
            for dx, dy in directions:
                for step in range(1, K + 1):
                    nx, ny = x + step * dx, y + step * dy
                    if 0 <= nx < N and 0 <= ny < M:
                        if grid[nx][ny] == '#':
                            break  # Stop at walls
                        new_can_dash = grid[nx][ny] == '*'  # Reset dash if landing on a crystal
                        if (nx, ny, new_can_dash) not in visited:
                            visited.add((nx, ny, new_can_dash))
                            queue.append((nx, ny, new_can_dash, moves + 1))
                        if (nx, ny) == end:
                            break  # Stop dash if reaching the end
                    else:
                        break  # Stop at grid boundaries

    # If we exhaust the queue without reaching the end
    return -1

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    index = 1
    results = []
    for _ in range(T):
        N, M, K = map(int, data[index].split())
        index += 1
        grid = [data[index + i] for i in range(N)]
        index += N
        results.append(solve(N, M, K, grid))
    
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
