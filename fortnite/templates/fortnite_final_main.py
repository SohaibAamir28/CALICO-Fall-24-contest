def solve(N, H, D, S, P):
    """
    Calculate the minimum time to exit the storm while maintaining non-negative health.
    N: Initial health
    H: Health gained per second when healing
    D: Distance to exit the storm (meters)
    S: Running speed (meters per second)
    P: Damage taken per second in the storm
    """
    import math
    
    # Time to run directly to the exit
    time_to_exit = D / S
    # Health remaining after running directly to the exit
    health_remaining = N - P * time_to_exit
    
    if health_remaining >= 0:
        return time_to_exit  # Can exit directly without additional healing
    
    # If direct exit is not possible, try to determine if intermittent healing helps
    # Set an arbitrary large number for minimum_time in case no solution is found
    min_time = float('inf')
    
    # Try different durations of healing and running
    for healing_time in range(0, 1001):  # Arbitrary large number to cap iterations
        # Total health after healing for 'healing_time' seconds
        health_after_healing = N + (H - P) * healing_time
        # Time to exit after healing
        if health_after_healing >= 0:
            time_needed_to_exit = D / S
            total_health_needed = P * time_needed_to_exit
            # Check if healed enough to sustain the run after healing
            if health_after_healing >= total_health_needed:
                total_time = healing_time + time_needed_to_exit
                if total_time < min_time:
                    min_time = total_time
    
    if min_time == float('inf'):
        return -1.0  # If no valid strategy was found
    
    return min_time

# Example usage within the provided `main` function
def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    index = 0
    T = int(data[index])
    index += 1
    results = []
    for _ in range(T):
        N = int(data[index])
        H = int(data[index + 1])
        D = int(data[index + 2])
        S = int(data[index + 3])
        P = int(data[index + 4])
        index += 5
        result = solve(N, H, D, S, P)
        results.append(result)
    for result in results:
        return (f"{result:.6f}")

if __name__ == '__main__':
    main()
