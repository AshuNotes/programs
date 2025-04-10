def dfs_with_depth_limit(start, goal, depth_limit):
    """
    Depth-First Search with a depth limit for the 8-puzzle.
    """
    def dfs(state, path, depth):
        if state == goal:
            return path + [state]
        if depth == 0:
            return None

        for move, new_state in get_moves(state):
            if new_state not in path: #prevent loops
                result = dfs(new_state, path + [state], depth - 1)
                if result:
                    return result
        return None

    return dfs(start, [], depth_limit)

def get_moves(state):
    moves, idx = [], state.index(0)
    directions = {'U': -3, 'D': 3, 'L': -1, 'R': 1}
    for move, d in directions.items():
        new_idx = idx + d
        if 0 <= new_idx < 9 and not (idx % 3 == 0 and move == 'L') and not (idx % 3 == 2 and move == 'R'):
            new_state = state[:]
            new_state[idx], new_state[new_idx] = new_state[new_idx], new_state[idx]
            moves.append((move, new_state))
    return moves

def print_solution(solution):
    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for i in range(0, 9, 3):
                print(*state[i:i+3])
            print()
    else:
        print("No solution found.")

start = [1, 2, 0, 4, 5, 3, 7, 8, 6]  # Example start state
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Goal state
depth = 3  # increased depth for finding the solution.
solution = dfs_with_depth_limit(start, goal, depth)

if solution:
    print_solution(solution)
    print("Solution Path:", solution)
else:
    print("No solution found.")