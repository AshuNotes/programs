from collections import deque

def uniform_cost_search(start, goal):
    queue, visited = deque([(0, start, [])]), set()
    while queue:
        cost, state, path = queue.popleft()
        if state == goal:
            return path + [state]
        visited.add(tuple(state))
        for move, new_state in get_moves(state):
            if tuple(new_state) not in visited:
                queue.append((cost + 1, new_state, path + [state]))
                queue = deque(sorted(queue, key=lambda x: x[0]))  # Sort by cost
    return None

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
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for i in range(0, 9, 3):
            print(*state[i:i+3])
        print()

start = [1, 2, 0, 4, 5, 3, 7, 8, 6]  # Example start state
goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Goal state
solution = uniform_cost_search(start, goal)

if solution:
    print_solution(solution)
    print("Solution Path:", solution)
else:
    print("No solution found.")