def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    table = {}
    if length == 1:
        return

    for i, weight in enumerate(weights):
        print(f"{weight} at index {i}")
        table[weight] = i

    for weight in weights:
        answer = [None] * 2
        entry_to_find = limit - weight
        if entry_to_find in table:
            print(f"entry to find: {entry_to_find}, weight: {weight}")
            if (length == 2) and (weight == entry_to_find):
                print(f'edge-case: {table[weight]}')
                answer[0] = table[weight]
                answer[1] = weights.index(weight)
            elif weight == limit:
                answer[0] = table[entry_to_find]
                answer[1] = table[weight]
            else:
                if weight >= entry_to_find:
                    answer[0] = table[weight]
                    answer[1] = table[entry_to_find]
                else:
                    answer[0] = table[entry_to_find]
                    answer[1] = table[weight]
            print(answer, 'the answer')
            return answer
    return None

