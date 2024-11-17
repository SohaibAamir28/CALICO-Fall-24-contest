from collections import deque

def find_minimum_moves(N: int, M: int, K: int, grid: list) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Find start (S) and end (E) positions
    start, end = None, None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j, True)  # (x, y, can_dash)
            elif grid[i][j] == 'E':
                end = (i, j)
    
    if not start or not end:
        return -1

    # BFS to find the shortest path
    queue = deque([(start[0], start[1], start[2], 0)])  # (x, y, can_dash, moves)
    visited = set((start[0], start[1], start[2]))

    while queue:
        x, y, can_dash, moves = queue.popleft()
        
        if (x, y) == end:
            return moves
        
        # Try walking to each adjacent tile
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != '#' and (nx, ny, can_dash) not in visited:
                visited.add((nx, ny, can_dash))
                queue.append((nx, ny, can_dash, moves + 1))

        # Try dashing if possible
        if can_dash:
            for dx, dy in directions:
                for step in range(1, K + 1):
                    nx, ny = x + step * dx, y + step * dy
                    if not (0 <= nx < N and 0 <= ny < M) or grid[nx][ny] == '#':
                        break
                    new_can_dash = grid[nx][ny] == '*' or can_dash
                    if (nx, ny, new_can_dash) not in visited:
                        visited.add((nx, ny, False))  # After dash, can_dash is False
                        queue.append((nx, ny, False, moves + 1))

    return -1

def main():
    T = int(input())
    for _ in range(T):
        N, M, K = map(int, input().split())
        grid = [input().strip() for _ in range(N)]
        print(find_minimum_moves(N, M, K, grid))

if __name__ == '__main__':
    main()
