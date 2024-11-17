def solve(B: int, N: int, S: list) -> int:
    '''
    Return the height H in which the danger is minimized and satisfies the budget constraints.
    '''
    min_height = min(S)
    max_height = max(S)
    best_height = -1
    min_danger = float('inf')
    min_cost = float('inf')

    for h in range(min_height, max_height + 1):
        danger = sum(h - s for s in S if s < h)
        cost = sum(s - h for s in S if s > h)

        if cost <= B:
            if danger < min_danger or (danger == min_danger and cost < min_cost):
                min_danger = danger
                min_cost = cost
                best_height = h

    return best_height


def main():
    T = int(input())
    for _ in range(T):
        temp = input().split()
        B, N = int(temp[0]), int(temp[1])
        S = [int(x) for x in input().split()]
        print(solve(B, N, S))


if __name__ == '__main__':
    main()
