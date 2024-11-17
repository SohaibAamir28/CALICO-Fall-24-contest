from fractions import Fraction

def solve(N: int) -> tuple[int, int]:
    houses = []
    slopes = set()

    x = 1
    while len(houses) < N:
        for y in range(1, x + 1):
            slope = Fraction(y, x)
            if slope not in slopes:
                houses.append((x, y))
                slopes.add(slope)
        x += 1

    # Define sorting key functions for Manhattan distance and x-coordinate
    def manhattan_distance(point):
        x, y = point
        return x + y

    def sorting_key(point):
        distance = manhattan_distance(point)
        x = point[0]
        return (distance, x)

    # Sort houses by Manhattan distance and then by x-coordinate
    houses.sort(key=sorting_key)

    # Return the N-th house's coordinates (1-indexed)
    return houses[N - 1]

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        # Print the coordinates for each test case
        print(*solve(N))

if __name__ == "__main__":
    main()