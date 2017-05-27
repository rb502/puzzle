start_state = [3, 8, 6, 2, 1, 4, 0, 7, 5]
end_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Probably should think of a better way of calculating the available moves, but this
# works for now.


def next_states(current_state):
    empty_idx = current_state.index(0)
    allowed_moves = []

    if empty_idx == 0:
        allowed_moves.append(1)
        allowed_moves.append(3)
    elif empty_idx == 1:
        allowed_moves.append(1)
        allowed_moves.append(-1)
        allowed_moves.append(3)
    elif empty_idx == 2:
        allowed_moves.append(-1)
        allowed_moves.append(3)
    elif empty_idx == 3:
        allowed_moves.append(1)
        allowed_moves.append(-3)
        allowed_moves.append(3)
    elif empty_idx == 4:
        allowed_moves.append(1)
        allowed_moves.append(-1)
        allowed_moves.append(3)
        allowed_moves.append(-3)
    elif empty_idx == 5:
        allowed_moves.append(-3)
        allowed_moves.append(3)
        allowed_moves.append(-1)
    elif empty_idx == 6:
        allowed_moves.append(-3)
        allowed_moves.append(1)
    elif empty_idx == 7:
        allowed_moves.append(-3)
        allowed_moves.append(-1)
        allowed_moves.append(1)
    elif empty_idx == 8:
        allowed_moves.append(-3)
        allowed_moves.append(-1)

    states = []
    for i in allowed_moves:
        new_pos = empty_idx + i
        if new_pos > 8 or new_pos < 0:
            continue

        new_state = current_state[:]
        new_state[empty_idx] = new_state[new_pos]
        new_state[new_pos] = 0

        if new_state not in states:
            states.append(new_state)

    return states


def breadth_first_search():
    queue = [[start_state]]
    visited = set()

    while queue:
        path = queue.pop(0)
        node = path[-1]

        if node == end_state:
            return path

        for next_state in next_states(node):
            if str(next_state) not in visited:
                new_path = list(path)
                new_path.append(next_state)
                queue.append(new_path)
                visited.add(str(next_state))


result = breadth_first_search()
print(len(result), '=>', result)
