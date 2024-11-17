from fractions import Fraction

def solve(N: int) -> tuple[int, int]:
    """
    Return a tuple containing the coordinates X and Y for the given address N.
    """
    def findHouseCoord(N):
        # Generate possible coordinates and filter based on visibility
        houses = []
        slopes = set()

        # Set x, y up to a reasonable limit
        limit = 100
        for x in range(1, limit + 1):
            for y in range(1, limit + 1):
                slope = Fraction(y, x)

                # If this slope hasn't been encountered before, it's visible (another house/coord isnt blocking it)
                if slope not in slopes:
                    houses.append((x, y))
                    slopes.add(slope)

        # Define sorting key functions
        def manhattan_distance(point):
            x, y = point
            return x + y

        def sorting_key(point):
            distance = manhattan_distance(point)
            x = point[0]
            return (distance, x)

        # Sort houses by Manhattan distance and then by x-coordinate
        houses.sort(key=sorting_key)

        # Return the coordinates for the given address N
        return houses[N - 1]
    
    # Get the coordinates for address N
    return findHouseCoord(N)

def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        # Print the coordinates for each test case
        print(*solve(N))

if __name__ == "__main__":
    main()