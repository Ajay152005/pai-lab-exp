def water_jug_problem(capacity_a, capacity_b, target_quantity):
    state = (0, 0)
    visited_states = set()
    actions = []

    def fill_jug_a(state):
        return (capacity_a, state[1])
    def fill_jug_b(state):
        return (state[0], capacity_b)
    def empty_jug_a(state):
        return (0, state[1])
    def empty_jug_b(state):
        return (state[0], 0)
    def pour_a_to_b(state):
        transfer = min(state[0], capacity_b - state[1])
        return (state[0] - transfer, state[1] + transfer)
    def pour_b_to_a(state):
        transfer = min(capacity_a - state[0], state[1])
        return (state[0] + transfer, state[1] - transfer)
    def goal_state(state):
        return state[0] == target_quantity or state[1] == target_quantity  # Check if either jug contains the target quantity

    def solve(state, actions):
        if goal_state(state):
            return actions
        visited_states.add(state)
        possible_actions = [fill_jug_a, fill_jug_b, pour_a_to_b, pour_b_to_a, empty_jug_a, empty_jug_b]  # Corrected the order of actions
        for action in possible_actions:
            next_state = action(state)
            if next_state not in visited_states:
                new_actions = actions + [action.__name__]
                result = solve(next_state, new_actions)
                if result:
                    return result
        return False

    solution = solve(state, [])
    if solution:
        return solution
    else:
        return "No Solution Found"

capacity_a = int(input("Enter the capacity of jug 1: "))
capacity_b = int(input("Enter the capacity of jug 2: "))
target_quantity = int(input("Enter the target quantity: "))

if target_quantity <= max(capacity_a, capacity_b):
    solution = water_jug_problem(capacity_a, capacity_b, target_quantity)
    if solution != "No Solution Found":
        for action in solution:
            print(action)
    else:
        print(solution)
else:
    print("Target quantity is not achievable with the given jug capacities.")
