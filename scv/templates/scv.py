def solve(M: int, N: int, G: list) -> str:
    """
    Return the shape of displayed by ASCII string G of dimensions N x M
    
    G: a string representing an ASCII picture
    N: integer for number of rows
    M: integer for number of columns

    Phineas = triangle
    Ferb = square
    """
    # YOUR CODE HERE
    rowCount = []

    # Check if each row has exactly M columns and count '#' characters
    for row in G:
        rowCount.append(row.count('#'))

    # Remove rows that have no '#' characters
    rowCount = [count for count in rowCount if count > 0]

    # Check if all row counts are the same (rectangle)
    if all(count == rowCount[0] for count in rowCount):
        print("ferb")
        return
    
    # Check if the shape is a triangle by checking for increasing or decreasing pattern
    isIncreasing = True
    for i in range(len(rowCount) - 1):
        if rowCount[i] >= rowCount[i + 1]:
            isIncreasing = False
            break

    isDecreasing = True
    for i in range(len(rowCount) - 1):
        if rowCount[i] <= rowCount[i + 1]:
            isDecreasing = False
            break

    if isIncreasing or isDecreasing:
        print("phineas")
        return

def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        G = []
        for _ in range(N):
            row = list(input().strip())
            G.append(row)
        solve(N, M, G)

if __name__ == '__main__':
    main()